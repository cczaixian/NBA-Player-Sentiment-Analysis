import json
import twython
import os
import requests
import time
import pandas as pd

CONSUMER_KEY = 'zgPC7n7fEAJuPLQvnM5QvrJZA'
CONSUMER_SECRET = 'zGZnfNPEqqCR2ucrSal9kUPSE7PRCqF6gRNkWckYMImlhXoKtl'
ACCESS_KEY = "257783857-3aba5yMJyg3w5DiNe9nJcEvk4cxPbRh73iiXT6e9"
ACCESS_SECRET = "blsUHUCouvON61RT4h5Fqwe0P0pIPcjNvRAcOJTbhipGV"
# create my_twitter folder
if not os.path.exists('my_twitter'):os.mkdir('my_twitter')

twitter = twython.Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
# screen_name, player's twitter name; start_id, the oldest tweet id; max_id, the latest tweet id

filname = "russwest44"

lis = [586377884752674816] ## this is the tweet id since 2015.4.15
sublist = []
for i in range(0, 5): # iterate through 1,000 tweets
## tweet extract method with the last list item as the max_id
    user_timeline = twitter.get_user_timeline(screen_name=filname, count=200, include_retweets=False, max_id=lis[-1])
# put info into json file
    for dict in user_timeline:
        # get 'text' and date 'created_at'
        subdict = {'date':dict['created_at'],'text':dict['text']}
        sublist.append(subdict)
# output json file in a pretty style
    output = open('my_twitter/'+str(filname) + '.json','w')
    json.dump(sublist,output,indent=4)
    output.close()

    for tweet in user_timeline:
        lis.append(tweet['id']) ## append tweet id's






"""
lis = [530102905635102720]
for i in range(0,2):
    home_timeline = twitter.get_user_timeline(screen_name='@sergeibaka9',count=200,max_id = [-1], include_rts=False)
    time.sleep(10)
# save into json file
    for i in home_timeline:
        print i
        lis.append(i['id'])

fwriter = open('my_twitter/'+ 'Harden13' +".json","w")

fwriter.write(json.dumps(home_timeline))
fwriter.close()
"""