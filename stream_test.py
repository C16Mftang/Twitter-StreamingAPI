from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import tweepy

access_token = "1055460403487084544-Lx3zS4sgqBpiGxZdCKFLqnA0NCCTcT"
access_token_secret = "XfF3Yj5ew9mNncQq2BCn6yAFBnlcBtpufrTXTted1K6i5"
API_key = "lk3h67VHklUtCHGmGBGInA1TL"
API_secret_key = "Ev7ENmQEm71QfznkXpMuh0dl0hbJyK1NedCSdAW36lhAXRa8U2"

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
