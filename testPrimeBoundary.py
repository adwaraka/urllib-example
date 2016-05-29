from src.url_parser import *
import unittest
import time

REMOTE_PRIME_TEST_LINK = 'http://findthebug.herokuapp.com/primenumbers'

class TestJudgePrimeAPI(unittest.TestCase):
    def setUp(self):
	    self.s = RemoteCall(REMOTE_PRIME_TEST_LINK)
		
    def testWithZero(self): #should probably give some other value for out-of-range values instead of false
        input_number = 0
        expected_output = 'false'
        actual_output = self.s.judgePrimeOrNot(input_number)
        time.sleep(5)
        self.assertEqual(expected_output, actual_output)		
    
    def testPrimeNumberOutOfRange(self): #should probably give some other value for out-of-range values instead of false
        input_number = 1013
        expected_output = 'false'
        actual_output = self.s.judgePrimeOrNot(input_number)
        time.sleep(5)
        self.assertEqual(expected_output, actual_output)

    def testCompNumberOutOfRange(self): #should probably give some other value for out-of-range values instead of false
        input_number = 1012
        expected_output = 'false'
        actual_output = self.s.judgePrimeOrNot(input_number)
        time.sleep(5)
        self.assertEqual(expected_output, actual_output)
		
    def testWithOne(self):
        input_number = 1
        expected_output = 'false'
        actual_output = self.s.judgePrimeOrNot(input_number)
        time.sleep(5)
        self.assertEqual(expected_output, actual_output)
		
    def testWithThousand(self):
        input_number = 1000
        expected_output = 'false'
        actual_output = self.s.judgePrimeOrNot(input_number)
        time.sleep(5)
        self.assertEqual(expected_output, actual_output)
		
    def testCompositeNumber(self):
        input_number = 90
        expected_output = 'false'
        actual_output = self.s.judgePrimeOrNot(input_number)
        time.sleep(5)
        self.assertEqual(expected_output, actual_output)
		
    def testPrimeNumber(self):
        input_number = 11
        expected_output = 'true'
        actual_output = self.s.judgePrimeOrNot(input_number)
        time.sleep(5)
        self.assertEqual(expected_output, actual_output)
		
if __name__ == '__main__':
    unittest.main()