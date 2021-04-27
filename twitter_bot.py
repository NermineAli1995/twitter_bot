import tweepy
import os
from os import environ

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

def retrieve_last_seen_id(file_name):
  f_read = open(file_name, 'r')
  last_seen_id = int(f_read.read().strip())
  f_read.close()
  return last_seen_id

def store_last_seen_id(last_seen_id,file_name):
  f_write = open(file_name, 'w')
  f_write.write(str(last_seen_id))
  f_write.close()
  return
