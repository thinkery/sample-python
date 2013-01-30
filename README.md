sample-python
=============

How to access the thinkery API using Python.

We provide a very small library (heavily inspired by [requests-oauth2](https://github.com/maraujop/requests-oauth2)) which uses a username/password combination to authenticate against the api. You can also use a web flow (and the url provided by `API.authorize_url()`) to get an access token.

Our sample program can be used to add a thing:

```
$ python add-thing.py "test thing" -t foo bar
{"_id":"31293a4c1cb602d812621129","title":"test thing","date":1359560000,"tags":["foo","bar"]}
```
(the response is the raw output from the api, which shows the thing that has been added successfully)

Requirements
------------

To use the API, you must create your API keys at http://thinkery.me/api/apps/

Also the [requests](https://github.com/kennethreitz/requests) library is being used. You can install it like this:
```python
pip install requests
```

