from datetime import datetime,timedelta,time
import MySQLdb

class LogReader:

	prefix = '/stats/mylyn/discovery'
	prefixLength = len(prefix)

	entries = []

	def readFile(self, logFile):
		inp = open(logFile, "r")
		for line in inp.readlines():
			self.parseLine(line)

	def parseLine(self, line):
		entry = LogEntry()
		for field in line.split():
			if ( field.startswith(self.prefix) ):
				request = field[self.prefixLength+1:]
				for key_value_pair in request[request.find('?')+1:].split('&'):
					parsed = key_value_pair.split('=')
					setattr(entry, parsed[0], parsed[1])

		ts = line[line.find('[')+1:line.find(']')]
		# %z seems not supported, see http://stackoverflow.com/questions/526406/python-time-to-age-part-2-timezones/526450#526450
		request_datetime = datetime.strptime(ts[:-6], "%d/%b/%Y:%H:%M:%S") 
		offset = int(ts[-5:])
		delta = timedelta(hours = offset / 100 )
		request_datetime -= delta
		entry.timestamp = str(int(request_datetime.strftime("%s")))
		self.entries.append(entry)

class DBWriter:
	
	entries = []
	host = "localhost"
	user = "root"
	passwd = ""
	db = "test"
	unix_socket = "/var/lib/mysql/mysql.sock"

	def write(self):
		db = MySQLdb.connect(host=self.host, db = self.db, user = self.user, passwd = self.passwd, unix_socket = self.unix_socket )
		cursor = db.cursor()
		for entry in self.entries:
			cursor.execute("""INSERT INTO discovery_log_entry (id, discovery, product, buildId, os, arch, ws, nl, _timestamp) 
					  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, FROM_UNIXTIME(%s))""", 
					  (entry.id, entry.discovery, entry.product, entry.buildId, entry.os, entry.arch, entry.ws, entry.nl, entry.timestamp))
		cursor.close()
		db.commit()
					

class LogEntry:

	id = ''
	discovery = ''
	product = ''
	buildId = ''
	os = ''
	arch = ''
	ws = ''
	nl = ''
	timestamp = ''

if __name__ == "__main__":
	l = LogReader()
	l.readFile('test/data/log.txt')
	d = DBWriter()
	d.entries = l.entries
	d.write()
