import urllib2, requests

class RemoteCall:
    def __init__(self, link):
        self.url = link
		
    def reverseString(self, query):
        results = requests.post(self.url, params={'string': query}, headers={'User-Agent': 'Mozilla/5.0'})
        return results.text.strip('" \n')

    def judgePrimeOrNot(self, input_number):
        results = requests.post(self.url, params={'number': input_number}, headers={'User-Agent': 'Mozilla/5.0'})
        return results.text.strip('" \n')