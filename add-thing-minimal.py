import thinkery, config

api = thinkery.API(config.client_id, config.client_secret)
client = api.get_client()

response = client.post("thing/add", {'title': 'thing title', 'tags': 'foo bar'})
print(response.text)
