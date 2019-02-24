"""A simple programme for collecting data from the Twitter Streaming API
More imformation on https://developer.twitter.com/en/docs.html"""

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import tweepy

access_token = "your_access_token"
access_token_secret = "your_access_token_secret"
API_key = "your_API_key"
API_secret_key = "your_API_secret_key"

#Keywords you wanna search
keywords = ['Trump', 'Brexit']


class StdOutListener(StreamListener):

    def on_data(self, data):
        if any(x in json.loads(data)['text'].lower() for x in keywords):
            print (data)
            with open('data.txt', 'a') as file:
                file.write(data+'\n')
        return True

    def on_error(self, status):
        print (status)

        
l = StdOutListener()
auth = OAuthHandler(API_key, API_secret_key)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)

#There are different parameters of filter; however, they can only be linked by "OR" conditions
stream.filter(keywords=keywords)

file.close()
