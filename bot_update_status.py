#
import tweepy

# Import Twitter Apps Configuration file from config.py file
from config import *


# Authenticate using keys & accesstoken
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Update status!
api.update_status(status="Today's keyword is #GameJam. Happy Saturday!")