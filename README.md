sample-python
=============

How to access the thinkery API using Python.

We provide a very small library (heavily inspired by https://github.com/maraujop/requests-oauth2) which uses a username/password combination to authenticate against the api. You can also use a web flow (and the url provided by `API.authorize_url()`) to get an access token.

Our sample program can be used to add a thing:

```
$ python add-thing.py "test thing" -t foo bar
{"_id":"31293a4c1cb602d812621129","title":"test thing","date":1359560000,"tags":["foo","bar"]}

```

Requirements
============

```python
pip install requests
```

