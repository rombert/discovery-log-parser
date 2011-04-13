import unittest
from DiscoveryParser import *

class LogParserTestCase(unittest.TestCase):
	def test_parseLines(self):
		r = LogReader()
		r.readFile('test/data/log.txt')
		
		self.assertEquals(4, len(r.lines))
		self.assertEquals("com.foglyn?id=com.foglyn&discovery=3.5.0&product=com.adobe.flexbuilder.standalone.product&os=win32&arch=x86&ws=win32&nl=en_US", r.lines[0])

	
if __name__ == "__main__":
    unittest.main()   

