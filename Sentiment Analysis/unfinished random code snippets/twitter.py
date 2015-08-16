import tweepy
from tweepy import StreamListener
from datetime import *
import re


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)





yesterday = date.today() - timedelta(hours=24)


consumer_key="kM6QNIld41CCYJisPTECdN6Yp"
consumer_secret = "DtPBjdvPi7b4qCOjQqRIpKNeQLOAPDS1DIuS0RCs0jlE6fMkG6"
access_token = "3382848435-mePu89dSShZFXgD74KZNpGXZ9I2c5HBE7LkhfYR"
access_token_secret = "5RErKexnXm83lzUoakX9d4XLurhgUqeZHxufTzZfcLRtu"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

listen = MyStreamListener(api)
myStream = tweepy.Stream(auth, listen)



#myStream.filter(languages=["en"], track=["games", "politics", "hacking", "education", "economics"])
print "================"



##public_tweets = api.home_timeline()
##for tweet in public_tweets:
##    print tweet.text

# Extract the first "xxx" tweets related to "fast car"
##
for tweet in tweepy.Cursor(api.search, q='en/books',languages=["en"], since='2015-07-28', until=date.today()).items(200): # need to figure out how to extract all tweets in the previous day
    result = re.sub(r"http\S+", "", tweet.text)
    result = re.sub(r"#\S+", "", result)
    print "================================"
    print result
    print "================================"
    
