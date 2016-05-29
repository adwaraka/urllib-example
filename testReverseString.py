from src.url_parser import *
import unittest
import time

REMOTE_REVERSE_STRING_LINK = 'http://findthebug.herokuapp.com/reversewords'

class TestReverseAPI(unittest.TestCase):
    def setUp(self):
	    self.s = RemoteCall(REMOTE_REVERSE_STRING_LINK)
		
    def testNoneInputReversal(self):
        input_string = None
        expected_output = '{"message": "The browser (or proxy) sent a request that this server could not understand."}'
        actual_output = self.s.reverseString(input_string)
        time.sleep(5)
        self.assertEqual(expected_output, actual_output)

    def testEmptyInputReversal(self):
        input_string = ''
        expected_output = ''
        actual_output = self.s.reverseString(input_string)
        time.sleep(5)
        self.assertEqual(expected_output, actual_output)
		
    def testSingleWordReversal(self):
        input_string = 'abcdefghijklmnopqrstuvwxyz'
        expected_output = 'zyxwvutsrqponmlkjihgfedcba'
        actual_output = self.s.reverseString(input_string)
        time.sleep(5)
        self.assertEqual(expected_output, actual_output)
		
    def testSingleWordReversalWithCases(self): #FAILED
        input_string = 'AbcdefghijkLmnopqrstuvwxyz'
        expected_output = 'zyxwvutsrqponmLkjihgfedcbA'
        actual_output = self.s.reverseString(input_string)
        time.sleep(5)
        self.assertEqual(expected_output, actual_output)
		
    def testMultipleWordReversal(self):
        input_string = 'the quick brown fox'
        expected_output = 'eht kciuq nworb xof'
        actual_output = self.s.reverseString(input_string)
        time.sleep(5)
        self.assertEqual(expected_output, actual_output)
		
    def testMultipleWordReversalWithCases(self): #FAILED
        input_string = 'The Quick Brown Fox'
        expected_output = 'ehT kciuQ nworB xoF'
        actual_output = self.s.reverseString(input_string)
        time.sleep(5)
        self.assertEqual(expected_output, actual_output)
		
    def testSingleWordDiffDelimReversal(self): #FAILED
        input_string = 'Whatssup!!'
        expected_output = 'pusstahW!!'
        actual_output = self.s.reverseString(input_string)
        time.sleep(5)
        self.assertEqual(expected_output, actual_output)
		
    def testMultipleWordsDiffDelimReversal(self): #FAILED
        input_string = 'the quick brown fox - did nothing!!'
        expected_output = 'eht kciuq nworb xof - did gnihton!!'
        actual_output = self.s.reverseString(input_string)
        time.sleep(5)
        self.assertEqual(expected_output, actual_output)

if __name__ == '__main__':
    unittest.main()