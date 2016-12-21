import tweepy
from textblob import TextBlob
from tweepy.auth import OAuthHandler

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('#RwOT')

for tweet in public_tweets:
	print(tweet)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
