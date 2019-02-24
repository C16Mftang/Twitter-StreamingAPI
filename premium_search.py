# -*- coding: utf-8 -*-
#This programme is for collecting Twitter data from the Search API
#Read the comment through carefully before run it
#Because of waste of rate limits
#For more info, https://developer.twitter.com/en/docs.html

import base64
import requests

client_key = "your-client-key"
client_secret = "your-client-secret"

#These following steps are to create a Bearer Token to use in the subsequent API requests
key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

#And this is to be used as the Bearer Token
Bearer_token = auth_resp.json()["access_token"]

#Now search
#These first 3 parameters are public, pre-defined before the request
search_headers = {'Authorization': 'Bearer {}'.format(Bearer_token)}
search_url = '{}1.1/tweets/search/fullarchive/boroughs.json'.format(base_url)
file = open('sample_data_2.txt', 'w')

#Search queries
#Initialise the request loop by start the first 100 tweets, to get a first next value
search_params = {'query': 'from: 355994177',
                 'fromDate': '201810250000',
                 'toDate': '201901250000',
                 'maxResults': '100'}
search_resp = requests.get(search_url, params=search_params, headers=search_headers)
tweets = search_resp.json()
print (tweets)

#Because of the limit of Tweets on each "page" of the collected data, need to iterate over several loops to get enough data
#The pages are collected by a 'next' value
#Now start the loop
#next time do this, comment this bit out to test, to avoid waste
next_value = first_next
j = 0
while j <= 1:
    search_params = {'query': 'congestion bounding_box:[-0.278622 51.431943 0.119429 51.604172]',
                     'fromDate': '201810270000',
                     'toDate': '201811270000',
                     'maxResults': '100',
                     'next': next_value}
    search_resp = requests.get(search_url, params=search_params, headers=search_headers)
    tweets = search_resp.json()
    print (tweets)
    j += 1

file.close()
