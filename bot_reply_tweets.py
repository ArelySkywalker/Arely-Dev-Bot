import tweepy

# Import Twitter Apps Configuration file from config.py file
from config import *

# Authentication using keys & accestoken
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

twt = api.search(q="Hello")

# list of strings that we want to check from tweets
txt = ['Hello',
        'Hello!',
        'Hello!!',
        'Hello,']

# Iteration can take some tiem
# TODO: Let's make this function better and more efficient
for st in twt:
	for s in txt:
		if s == st.text:
			usr = st.user.screen_name
			msg = ("@%s Hello!" %(usr))
			st = api.update_status(msg, st.id)