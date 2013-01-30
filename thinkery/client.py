import requests
from urllib import quote

class Client(object):
	site = 'https://api.thinkery.me/v1/'

	def __init__(self, access_token):
		"""
		Initializes the API client with the necessary info
		"""
		self.r = requests.session(params={'access_token': access_token})

	def get(self, call):
		"""
		Issue a GET request against the thinkery API
		"""
		return self.r.get("%s%s" % (self.site, quote(call)))

	def post(self, call, params):
		"""
		Issue a POST request against the thinkery API
		"""
		return self.r.post("%s%s" % (self.site, quote(call)), params)
