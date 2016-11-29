import tweepy
import pandas as pd
import json
import time
    

consumer_key = ...
consumer_secret = ...
access_token = ...
access_token_secret = ...

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
    
MAX_TWEETS = 10

data = tweepy.Cursor(api.search, q='hashtag').items(MAX_TWEETS)
 
datalist = []
 
for tweet in data:   #tweet.json resource
    datalist.append(json.loads(json.dumps(tweet._json)))
           
           
# Create the dataframe we will use
tweets = pd.DataFrame()
# What is the tweet's content
tweets['text'] = map(lambda tweet: tweet['text'].encode('utf-8'), datalist)
# If available what is the language the tweet is written in
tweets['lang'] = map(lambda tweet: tweet['lang'], datalist)
# If available, where was the tweet sent from ?
tweets['Location'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, datalist)

print tweets