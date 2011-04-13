class LogReader:

	prefix = '/stats/mylyn/discovery'
	prefixLength = len(prefix)

	lines = []

	def readFile(self, logFile):
		inp = open(logFile, "r")
		for line in inp.readlines():
			for field in line.split():
				if ( field.startswith(self.prefix) ):
					self.lines.append(field[self.prefixLength+1:])

