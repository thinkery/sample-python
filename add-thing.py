import thinkery
import config
import argparse

parser = argparse.ArgumentParser(description='Add a thing to thinkery')
parser.add_argument('title', metavar='title', help='the thing title')
parser.add_argument('-url', metavar='u', nargs=1, help='url of the thing')
parser.add_argument('-tags', metavar='t', nargs='+', help='tags')
args = parser.parse_args()

api = thinkery.API(config.client_id, config.client_secret)
client = api.login(config.username, config.password)

params = vars(args)
params['tags'] = str.join(' ', params['tags'])

response = client.post("thing/add", params)
print response.text
