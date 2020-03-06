# coding=utf-8
import config
import tweepy

# Twitter API
CONSUMER_KEY = config.TW_CONSUMER_KEY
CONSUMER_SECRET = config.TW_CONSUMER_SECRET
ACCESS_TOKEN = config.TW_TOKEN
ACCESS_TOKEN_SECRET = config.TW_TOKEN_SECRET



text = 'test tweet4'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
api.update_status(status=text)