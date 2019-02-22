from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import tweepy

access_token = "your_access_token"
access_token_secret = "your_access_token_secret"
API_key = "your_API_key"
API_secret_key = "your_API_secret_key"

"""traffic_words = ['traffic jam', 'traffic', 'congest', 'congestion', 'congestion charge', 'jammed',
                 'gridlock', 'rush hour', 'transport', 'bottleneck']"""
traffic_words = ['traffic']


class StdOutListener(StreamListener):

    def on_data(self, data):
        #print (data)
        if any(x in json.loads(data)['text'].lower() for x in traffic_words):
            print (data)
            with open('streamdata1.txt', 'a') as file:
                file.write(data+'\n')
        return True

    def on_error(self, status):
        print (status)


#if __name__ == '__main__':
l = StdOutListener()
auth = OAuthHandler(API_key, API_secret_key)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)

stream.filter(follow=['47319664', '355994177'])

file.close()
