#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import tweepy
import time
import traceback
import urllib
import webbrowser
from tweepy.models import Status
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
#consumer_key= ["", ""]
#consumer_secret= ["", ""]
#access_token= ["", ""]
#access_token_secret= ["", ""]

NASDAQ_SYMBOL= "$ABT OR $ABBV OR $ACE OR $ACN OR $ACT OR $ADBE"
NASDAQ_COMPANY = "\"Abbott Laboratories\" OR \"AbbVie\" OR \"ACE Limited\" OR \"Accenture plc\" OR \"Actavis plc\" OR \"Adobe Systems Inc\""
NASDAQ_COMBINE = "$A Agilent Technologies Inc OR $AA Alcoa Inc OR $MO Altria Group Inc"
searchString = ""

#f= open("datafile.txt","a")
f=""
def collect(query, api1):
    global f
    #api = tweepy.API(auth)
    for tweet in tweepy.Cursor(api1.search, q=query, rpp=100, include_entities=True, wait_on_rate_limit=True).items(10000):
        f.write(str(tweet.created_at) + ", " + str(tweet.text.encode("utf-8")).replace('\n', ' ') + "\n")
            
def main():
    consumer_key = str(sys.argv[1])
    consumer_secret = str(sys.argv[2])
    access_token = str(sys.argv[3])
    access_token_secret = str(sys.argv[4])
    searchString = str(sys.argv[5])
    fpath = "/panasas/scratch/dileepra/" + str(sys.argv[6])
    print fpath
    print consumer_key
    print consumer_secret
    print access_token
    print access_token_secret
    searchString += ' since:2014-11-23 lang:en'
    print searchString
    global f
    f = open(fpath, "a")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    #print(api.rate_limit_status())
    query = (str(NASDAQ_SYMBOL) + ' OR ' + str(NASDAQ_COMPANY)  + ' since:2014-10-01 lang:en')
    #print query
    i = 0
    ex = 0
    counter = 0;
    while(1):
	i = (i+1) % 2 
        try:
	    counter = counter + 1
            print "Counter : " + str(counter) + "\n"
            collect(searchString, api)
        except:
	    traceback.print_exc()
            ex = ex + 1
	    if ex == 1:
	        time.sleep(60 * 15)
		ex = 0
            #auth = tweepy.OAuthHandler(consumer_key[i], consumer_secret[i])
            #auth.set_access_token(access_token[i], access_token_secret[i])
	
if __name__ == '__main__':
    main()
