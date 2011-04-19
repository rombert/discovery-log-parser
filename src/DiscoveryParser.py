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
