from matplotlib.pyplot import text
import tweepy
import re
import json
import wallet
import ElectionLib
import demoji
from deep_translator import GoogleTranslator

def clean(text):
   text = demoji.replace_with_desc(text)
   text = text.lower()
   return re.sub('(@[A-Za-z0-9_:.]+)|(rt)|(https:[A-Za-z0-9._/]+)|(#)|','',text)

api_key,api_secret_key,api_token,api_secret_token=wallet.twitterKeys()

OAUTH_KEYS = {'consumer_key':api_key, 'consumer_secret':api_secret_key,
 'access_token_key':api_token, 'access_token_secret':api_secret_token}

auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth)

bjp_keywords=['BJP','Bharatiya Janata Party','Narendra Modi','Modi']
inc_keywords=['INC','Indian National Congress','Rahul Gandhi','Manmohan Singh']

num = int(input("Enter number of tweets (try to use multiples of 8):"))
num = num / 8
for key in bjp_keywords:
   Tweets = tweepy.Cursor(api.search_tweets, q=key, tweet_mode="extended").items(num)

   for tweet in Tweets:
      try:
         if 'retweeted_status' in dir(tweet):
            full_text=tweet.retweeted_status.full_text
         else:
            full_text=tweet.full_text
      except:
         full_text=tweet.text

      if tweet.lang != 'en':
         full_text = GoogleTranslator(source='auto', target='en').translate(full_text)
         tweet.lang = 'en'

      print("Raw:",full_text)
      full_text=clean(full_text)
      print("Clean:",full_text)

      ElectionLib.importDataTwitter(tweet.id, full_text, tweet.created_at, tweet.geo, tweet.lang,'b',key)

for key in inc_keywords:
   Tweets = tweepy.Cursor(api.search_tweets, q=key, tweet_mode="extended").items(num)

   for tweet in Tweets:
      try:
         if 'retweeted_status' in dir(tweet):
            full_text=tweet.retweeted_status.full_text
         else:
            full_text=tweet.full_text
      except:
         full_text=tweet.text

      if tweet.lang != 'en':
         full_text = GoogleTranslator(source='auto', target='en').translate(full_text)
         tweet.lang = 'en'

      print("Raw:",full_text)
      full_text=clean(full_text)
      print("Clean:",full_text)
      ElectionLib.importDataTwitter(tweet.id, full_text, tweet.created_at, tweet.geo, tweet.lang,'i',key)
