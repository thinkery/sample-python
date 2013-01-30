import thinkery
import config

api = thinkery.API(config.client_id, config.client_secret)
client = api.login(config.username, config.password)

response = client.post("thing/add", {'title': 'thing title', 'tags': 'foo bar'})
print response.text
