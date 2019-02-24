# -*- coding: utf-8 -*-
#This programme is for looking for an efficient way to get data and produce the prototype
#for clean_data.py
#Read the comment through carefully before run it
#Because of waste!


import base64
import requests

client_key = "lk3h67VHklUtCHGmGBGInA1TL"
client_secret = "Ev7ENmQEm71QfznkXpMuh0dl0hbJyK1NedCSdAW36lhAXRa8U2"

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
#注意此处！下一次再用'a'的时候注意要新开一个文件，不然会重复写入（此处为900问题起源）
#下一次运行此程序时，先把参数改小，不然太浪费
#Initialise the request loop by start the first 100 tweets, to get a first next value
search_params = {'query': 'from: 355994177',
                 'fromDate': '201810250000',
                 'toDate': '201901250000',
                 'maxResults': '100'}
search_resp = requests.get(search_url, params=search_params, headers=search_headers)
tweets = search_resp.json()
print (tweets)
for i in tweets['results']:
    #This edit step is actually useless! just write i to the txt file and clean_data.py will do the rest
    file.write(str(i)+'\n')
#first_next = tweets['next']

#Now start the loop
#next time do this, comment this bit out to test, to avoid waste
'''
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
    for i in tweets['results']:
        file.write(str(i)+'\n')
    next_value = tweets['next']
    j += 1
'''

file.close()