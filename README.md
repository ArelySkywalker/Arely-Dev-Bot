# Dev Arely's Twitter Bot

[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

Twitter bot using Tweepy and Python.

Tweepy is a Python library which provide access to Twitter API.
## Installation 
``pip install tweepy``

## Usage
Before run any file please edit **[config.py](https://github.com/ArelySkywalker/Arely-Dev-Bot/blob/master/config.py)** file according to your **[Keys and access token](https://dev.twitter.com/oauth/overview/application-owner-access-tokens)**.

### Update Status

To upate your status, into bot_update_status.py and change status="This is my first tweet using python code!"

**TODO:** 

- [ ] Create a JSON file that has pre-made tweets. update_status will then take a random tweet from the file to update status so we don't have to manually change satus every time.

Run this command in your terminal:

``python bot_update_status.py``

Goto your Twitter account profile you can see result.

### Retweet by Keyword

``python bot_retweet.py``
