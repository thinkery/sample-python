import requests
from urllib import quote, urlencode
from urlparse import parse_qs
from thinkery.client import Client
try:
	import simplejson as json
except ImportError:
	import json

# heavily inspired by https://github.com/maraujop/requests-oauth2
class API(object):
	authorization_url = 'http://thinkery.me/api/authorize.php'
	token_url = 'token'
	site = 'https://api.thinkery.me/v1/'

	def __init__(self, client_id, client_secret, redirect_uri=None):
		"""
		Initializes the library with the necessary OAuth2 parameters
		"""
		self.client_id = client_id
		self.client_secret = client_secret
		self.redirect_uri = redirect_uri

	def authorize_url(self, scope='', **kwargs):
		"""
		Returns the url to redirect the user to for user consent
		"""
		params = {'redirect_uri': self.redirect_uri, 'client_id': self.client_id, 'scope': scope}
		params.update(kwargs)
		return "%s%s?%s" % (self.site, quote(self.authorization_url), urlencode(params))

	def login(self, username, password, **kwargs):
		"""
		Returns a new Client which can then be used to access the API
		"""
		url = "%s%s" % (self.site, quote(self.token_url))
		data = {'client_id': self.client_id, 'client_secret': self.client_secret, 'username': username, 'password': password, 'grant_type': 'password'}
		data.update(kwargs)
		response = requests.post(url, data=data)

		if isinstance(response.content, basestring):
			try:
				content = json.loads(response.content)
			except ValueError:
				content = parse_qs(response.content)
		else:
			content = response.content

		return Client(self.client_id, self.client_secret, content['access_token'])
