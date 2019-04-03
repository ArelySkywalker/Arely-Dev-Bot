# Retweet bot for Twitter using Python and Tweepy
# Search query via hashtag or keyword.

import tweepy

from time import sleep
# Import Twitter Apps Configuration file from config.py file
from config import *


# Authenticate using keys & accesstoken
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# q='#example', #example is the hashtach or keyword we want to search
# items(n), n is the number of retweets we want to tweet
for tweet in tweepy.Cursor(api.search, q='#SoftwareEngineering', result_type="mixed").items(5):
    try:
        print('\nRetweet Bot found tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to retweet.')
        tweet.retweet()
        print('Retweet publised successfully.')

        # sleep(n), is the sleep measured in seconds
        # this is the numbre of seconds we want to have in-between retweets
        sleep(10)

    # Some basic error handling. Will print out why retweet failed
    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)
    
    except StopIteration:
        break
