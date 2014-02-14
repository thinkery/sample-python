import requests, pickle, os
from urllib import quote, urlencode
from urlparse import parse_qs
from thinkery.client import Client

try:
	import simplejson as json
except ImportError:
	import json

# heavily inspired by https://github.com/maraujop/requests-oauth2
class API(object):
	authorization_url = 'https://thinkery.me/api/authorize.php'
	token_url = 'token'
	site = 'https://api.thinkery.me/v1/'
	logged_in = False
	access_token = None
	token_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'tokens.pkl')

	def __init__(self, client_id, client_secret, redirect_uri=None):
		"""
		Initializes the library with the necessary OAuth2 parameters
		"""
		self.client_id = client_id
		self.client_secret = client_secret
		self.redirect_uri = redirect_uri

		try:
			config = open(self.token_file, 'rb')
			data = pickle.load(config)
			config.close()
			if not self.test(data['access_token']):
				self.refresh_token(data['refresh_token'])
			self.logged_in = True
		except EOFError:
			return
		except IOError:
			return

	def authorize_url(self, scope='', **kwargs):
		"""
		Returns the url to redirect the user to for user consent
		"""
		params = {'redirect_uri': self.redirect_uri, 'client_id': self.client_id, 'scope': scope}
		params.update(kwargs)
		return "%s%s?%s" % (self.site, quote(self.authorization_url), urlencode(params))

	def test(self, access_token, **kwargs):
		"""
		Makes a test-request to the API to see if the access_token is still valid
		"""
		url = "%s%s" % (self.site, "test")
		data = {'client_id': self.client_id, 'client_secret': self.client_secret, 'access_token': access_token}
		data.update(kwargs)
		response = requests.post(url, data=data)

		if isinstance(response.content, basestring):
			try:
				content = json.loads(response.content)
			except ValueError:
				content = parse_qs(response.content)
		else:
			content = response.content

		if 'user' in content:
			self.access_token = access_token
			return True

		return False

	def refresh_token(self, refresh_token, **kwargs):
		"""
		Gets a new set of tokens using the given refresh_token
		"""
		url = "%s%s" % (self.site, quote(self.token_url))
		data = {'client_id': self.client_id, 'client_secret': self.client_secret, 'refresh_token': refresh_token, 'grant_type': 'refresh_token'}
		data.update(kwargs)
		response = requests.post(url, data=data)

		if isinstance(response.content, basestring):
			try:
				content = json.loads(response.content)
			except ValueError:
				content = parse_qs(response.content)
		else:
			content = response.content

		if 'access_token' not in content:
			raise IOError

		config = open(self.token_file, 'wb')
		pickle.dump(content, config)
		config.close()

		self.access_token = content['access_token']
		return Client(self.access_token)


	def get_client(self, **kwargs):
		return Client(self.access_token)

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

		if 'access_token' not in content:
			raise IOError

		config = open(self.token_file, 'wb')
		pickle.dump(content, config)
		config.close()

		self.access_token = content['access_token']
		return Client(self.access_token)
