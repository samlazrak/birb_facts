import tweepy
import random

from secrets import consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

birbFacts = [
  'Birbs have wings',
  'Birbs have beaks',
  'Birbs are Birbs',
  'Birbs like seeds',
  'I am a Birbs'
]

api.update_status(birbFacts[random.randint(0, 4)])