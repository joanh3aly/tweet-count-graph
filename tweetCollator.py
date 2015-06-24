#!/usr/bin/python
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import re
import sys
import json
import dateutil.parser
from pytz import timezone
import pytz
import numpy as np
import threading
import time

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
CONSUMER_KEY="hVXOnpdbN0uLtAUSEjOdUgL6b"
CONSUMER_SECRET="CWYDtRZTFJdN5WQO6WaVkNoLYDuWpBFilAhFZEnbqqQKMfDX8f"
ACCESS_TOKEN="1577934554-zSVtsvcwYW9t6ZWom8iBtlcim4R7YFoEvs4uoXy"
ACCESS_TOKEN_SECRET="6mX3Sf76QZurtpKzZHsiTE21n3V7RI1NkjdUntfKQwGxr"

# Put in your twitter search terms here
TERMS = [
   'Carter'
        ]
        
sgtz = timezone('Asia/Singapore')
utc = pytz.timezone('UTC')
        
regex = re.compile('|'.join(TERMS).lower())   # re.compile(pattern, flags=0)  Compile a regular expression pattern into a regular expression object, which can be used for matching using its match() and search() methods
linenum_re = re.compile(r'([A-Z][A-Z]\d+)')

retweets_re = re.compile(r'^RT\s')

enc = lambda x: x.encode('latin1', errors='ignore')  # lambda :	 creation of anonymous functions // .encode Encodes obj using the codec registered for encoding. The default encoding is 'ascii'.



class StdOutListener(StreamListener):
    def on_data(self, data):
        tweet = json.loads(data) # Deserialize (a str or unicode instance containing a JSON document) to a Python object 

        if not tweet.has_key('user'):   # key -- This is the Key to be searched in the dictionary.
            print 'No user data - ignoring tweet.'
            return True

        user = enc(tweet['user']['name']) # enc function from .encode into latin , line 118 above
        text = enc(tweet['text'])
        print "text"

        print text

        # ignore text that doesn't contain one of the keywords
        matches = re.search(regex, text.lower()) 	
        if not matches:
            return True

        # ignore retweets
        if re.search(retweets_re, text): # re_retweets from line 116 above - re.compile searches for RTs and this filters them out
            return True

        location = enc(tweet['user']['location'])
        source = enc(tweet['source'])
        d = dateutil.parser.parse(enc(tweet['created_at']))

        # localize time - you need to use the normalize() method to handle daylight saving time and other timezone transitions
        d_tz = utc.normalize(d)  
        #  building a localized time by converting an existing localized time using the standard astimezone() method
        localtime = d.astimezone(sgtz) 
        # time.strftime(format[, t]) - Convert a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string as specified by the format argument. returns a locale dependent byte string.
        tmstr = localtime.strftime("%Y%m%d-%H:%M:%S")  
        print "localtime %s." % localtime
        
        
        splittedString = tmstr.split('-')[1]
        hour = splittedString.split(':')[0]
        print('hour %s' % hour)
		
        # Find geolocation of tweeter
        geo = tweet['geo']  # tweet comes from json.loads(data) function
        print "geo"
        print geo
        
        # append the hourly tweet file
        with open('/Applications/MAMP/htdocs/social_test/twitter/network-map/station-tweet-data/carter2-%s.data' % tmstr.split(':')[0], 'a+') as g: 
            print("carter:  %s \t %s \n" % (tmstr,hour))
            g.write("carter:  \t %s \t %s \n" % (hour,text))
		
        # is this a geocoded tweet?
        if geo and geo['type'] == 'Point':   # see JSON format to see where 'POint' comes from 
            # collect location of mrt station
            coords = geo['coordinates']
            print "coords"
            print coords
            print coords[1]
      
       # print summary of tweet
        print('%s\n%s\n%s\n%s\n%s\n\n ----------------\n' % (user, location, source, tmstr, text))
		
        return True
        
   
    def on_error(self, status):
        print('status: %s' % status)




if __name__ == '__main__':  # run code in main file not from another module
    l = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    stream = Stream(auth, l, timeout=60)  #initialize Stream object with a time out limit

    print("Listening to filter stream...")
    print("stream object")
    print(stream)

    stream.filter(track=TERMS)  #call the filter method to run the Stream Object -- filter(function, iterable) - Construct a list from those elements of iterable for which function returns true. iterable may be either a sequence, a container which supports iteration, or an iterator
  
  
  #  stream.count(stream.filter(track=TERMS))
    
    
   

    