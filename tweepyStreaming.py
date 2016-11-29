from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

class StdOutListener(StreamListener):

    def on_data(self, data):
        #or save to db.
        with open('filePath/file.txt','a') as tf:
            tf.write(data)
        return True

    def on_error(self, status):
        print status

        
if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, StdOutListener())

    #This line filter Twitter Streams to capture data by the keywords list: 
    stream.filter(track=['python', 'javascript', 'ruby'])


datalist = []

tweets_file = open('filePath/file.txt', 'r')
for line in tweets_file:
    try:
        tweet = json.loads(line)
        datalist.append(tweet)
    except:
        continue

print len(datalist)
tweets = pd.DataFrame()
tweets['text'] = map(lambda tweet: tweet['text'].encode('utf-8'), datalist)
# If available what is the language the tweet is written in
tweets['lang'] = map(lambda tweet: tweet['lang'], datalist)
# If available, where was the tweet sent from ?
tweets['Location'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, datalist)

print tweets