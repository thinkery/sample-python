import thinkery
import config
import argparse
import getpass

parser = argparse.ArgumentParser(description='Add a thing to thinkery')
parser.add_argument('title', metavar='title', help='the thing title')
parser.add_argument('-url', metavar='u', nargs=1, help='url of the thing')
parser.add_argument('-tags', metavar='t', nargs='+', help='tags')
args = parser.parse_args()

api = thinkery.API(config.client_id, config.client_secret)

if not api.logged_in:
	username = raw_input("Username [%s]: " % getpass.getuser())
	if not username:
		username = getpass.getuser()
	password = getpass.getpass()
	client = api.login(username, password)
else:
	client = api.get_client()

params = vars(args)
if 'tags' in params and params['tags'] != None:
	params['tags'] = str.join(' ', params['tags'])

response = client.post("thing/add", params)
print response.text
