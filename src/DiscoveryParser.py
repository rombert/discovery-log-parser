from datetime import datetime,timedelta,time

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
