import requests
from urllib import quote, urlencode
from urlparse import parse_qs
try:
    import simplejson as json
except ImportError:
    import json

class Client(object):
    site = 'https://api.thinkery.me/v1/'

    def __init__(self, client_id, client_secret, access_token):
    	self.r = requests.session(params={'access_token': access_token})

    def get(self, call):
    	return self.r.get("%s%s" % (self.site, call))

    def post(self, call, params):
    	return self.r.post("%s%s" % (self.site, quote(call)), params)
