import requests
from urllib import quote

class Client(object):
	site = 'https://api.thinkery.me/v1/'

	def __init__(self, client_id, client_secret, access_token):
		"""
		Returns a new Client which can then be used to access the API
		"""
		self.r = requests.session(params={'access_token': access_token})

	def get(self, call):
		"""
		Issue a GET request against the thinkery API
		"""
		return self.r.get("%s%s" % (self.site, call))

	def post(self, call, params):
		"""
		Issue a POST request against the thinkery API
		"""
		return self.r.post("%s%s" % (self.site, quote(call)), params)
