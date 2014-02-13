import thinkery
import config

api = thinkery.API(config.client_id, config.client_secret)
if not api.logged_in:
	username = raw_input("Username [%s]: " % getpass.getuser())
	if not username:
		username = getpass.getuser()
	password = getpass.getpass()
	client = api.login(username, password)
else:
	client = api.get_client()

response = client.post("thing/add", {'title': 'thing title', 'tags': 'foo bar'})
print response.text
