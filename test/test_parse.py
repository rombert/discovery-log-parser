import unittest
from DiscoveryParser import *

class LogParserTestCase(unittest.TestCase):
	def test_parseLines(self):
		r = LogReader()
		r.readFile('test/data/log.txt')
		
		self.assertEquals(4, len(r.entries))

		entry = r.entries[0];
		self.assertEquals('com.foglyn', entry.id)
		self.assertEquals('3.5.0', entry.discovery)
		self.assertEquals('com.adobe.flexbuilder.standalone.product', entry.product)
                self.assertEquals('win32', entry.os)
                self.assertEquals('x86', entry.arch)
                self.assertEquals('win32', entry.ws)
                self.assertEquals('en_US', entry.nl)
		self.assertEquals('1302524564', entry.timestamp) # 2011-04-11 15:22:44 in Etc/GMT

	def test_skip_already_parsed(self):
		r = LogReader()
		r.lastTimestamp = 1302693588 # max timestamp from the log file
		r.readFile('test/data/log.txt')
		self.assertEquals(0, len(r.entries))
	
if __name__ == "__main__":
    unittest.main()   

