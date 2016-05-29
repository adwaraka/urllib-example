from src.url_parser import *
import unittest
import logging
import datetime
import time, os

REMOTE_PRIME_TEST_LINK = 'http://findthebug.herokuapp.com/primenumbers'

class TestJudgePrimeCompleteAPI(unittest.TestCase):
    ''' This is a comprehensive test case that checks whether all the values in the range are getting parsed and the correct
	ones are getting detected as prime. Logs for the process'''
    def setUp(self):
        t = datetime.datetime.now()
        logfile_name = 'prime_log_' + t.strftime('%Y%m%d%H%M%S') + '.log'
        if not os.path.exists('Logs\\'):
		    os.makedirs('Logs\\')
        logging.basicConfig(filename="Logs\\"+logfile_name, level=logging.INFO)
        self.s = RemoteCall(REMOTE_PRIME_TEST_LINK)
        self.expected_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
        self.actual_list = []
	
    def testPrimeNumber1to200(self):
        for input_number in xrange(1,201): #Slotted by batches of 200 because of my internet throwing a fit and dying every fifteen mins!!
            logging.info("Verifying {}...".format(input_number))
            actual_output = self.s.judgePrimeOrNot(input_number)
            time.sleep(5)
            if actual_output == 'true':
                logging.info("Added {} to the actual list. It is prime.".format(input_number))
                #Used findstr /i /c:"It is prime." example.log > result.out to isolate the values from the example.log added to the prime list
                self.actual_list.append(input_number)
            time.sleep(5)
        self.assertEqual(self.actual_list, self.expected_list)

    '''
    Planned to implement each of these as a batch and maintain their corresponding expected_list
	def testPrimeNumber201to400(self):
	def testPrimeNumber401to600(self):
	def testPrimeNumber601to800(self):
	def testPrimeNumber801to1000(self):
	'''

if __name__ == '__main__':
    unittest.main()