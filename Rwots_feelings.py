import tweepy
from textblob import TextBlob
from tweepy.auth import OAuthHandler

consumer_key = 'wEJI4Jc1IMQM6bgp0UV4eoCRD'
consumer_secret = 'Cx3Ha8OQX2J0b88v3X5P3XyYaaFz74i6xAGDLFInT6rGOeDDt1'

access_token = '743342539-nNnXIylLJUIsThfNDOomiOiRqJb9XrgZ5dUXiknK'
access_token_secret = 'AbpmtagoDIp6MFGxOgRAunFOjNRAU8cBFZSBBpgHBKqc5'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('#RwOT')

for tweet in public_tweets:
	print(tweet)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)