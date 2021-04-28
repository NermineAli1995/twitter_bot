import os
import time
from os import environ
import tweepy
from dotenv import load_dotenv

load_dotenv()

CONSUMER_KEY = environ.get("CONSUMER_KEY")
CONSUMER_SECRET = environ.get("CONSUMER_SECRET")
ACCESS_KEY = environ.get("ACCESS_KEY")
ACCESS_SECRET = environ.get("ACCESS_SECRET")


print("starting the service")
FILENAME_FAV = "id_favorite_tweet.txt" 


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

def fav_tweet():
  print("Retrieving Tagged Tweets...")
  last_seen_id = retrieve_last_seen_id(FILENAME_FAV)
  mentions = api.mentions_timeline(last_seen_id,tweet_mode='extended')
  for mention in reversed(mentions):
    if not mention:
      return
    print(str(mention.id)+' - '+mention.full_text)
    last_fav_tweet = mention.id
    store_last_seen_id(last_fav_tweet,FILENAME_FAV)
    api.create_favorite(mention.id)
    api.retweet(mention.id)
    print("Found @Ali1995Nermine")
    print("Liked and retweeted!")


while True:
  fav_tweet()
  time.sleep(15)
