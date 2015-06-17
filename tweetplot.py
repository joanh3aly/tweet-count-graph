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
from numpy import genfromtxt
import threading
import time
import csv
import datetime
#from datetime import datetime
from datetime import date
import matplotlib.pyplot as plt
from StringIO import StringIO
import pylab as pl
import matplotlib.pyplot as plt



def on_data():	
    # this condition needs to count how many tweets with defined subject matter/user id are tweeted per hour, and then store in a numpy array	
      
    # To create numpy array from CSV file - splits at tab   
    my_data = genfromtxt('/Applications/MAMP/htdocs/social_test/twitter/network-map/station-tweet-data/cj3-20150611-18.data', delimiter='\t',autostrip=True)
    print my_data
    hourRecorded = my_data[0,1]
    
    nineteen = []
    eighteen = []
    for index in range(len(my_data)):
        if(my_data[index][1] == 18):
          #  tweetNumber18 = my_data[index][1]
            eighteen.append(my_data[index][1])

        if(my_data[index][1] == 19):
            nineteen.append(my_data[index][1])
    
    
    
    # Count amount of records in Numpy array
    print eighteen
    print "eighteenLen"
    eighteenLen = len(eighteen) 
    print eighteenLen
    print "nineteenLen"
    nineteenLen = len(nineteen)
    print nineteenLen  
          
    print "hourRecorded"
    print hourRecorded
    
    hourRecordedNineteen = nineteen[0]
    print "hourRecordedNineteen"
    print hourRecordedNineteen
  
    # Create new NP array with hour and number of tweets
    hourlyTweetNo = np.array([[18, eighteenLen], [19, nineteenLen]])
    print('hourlytweets')
    print hourlyTweetNo
   
    return hourlyTweetNo
    
def plotter(NPtweetsperhour):
    print "NPtweetsperhour"
    print NPtweetsperhour[[0,1]]
    # Plot!!@@!!    
    plt.plot(NPtweetsperhour[[1]],NPtweetsperhour[[0]], 'ro')
    plt.axis([0, 24, 0, 200])
    plt.xlabel('hour', fontsize=18)
    plt.ylabel('tweet-volume', fontsize=18)
    plt.show()
    
    # to save the figure to a file
    # plt.savefig('/tmp/out.png')   	
    
    #  threading.Timer(60, f).start()
    
    return True
    

if __name__ == '__main__':  # run code in main file not from another module
    
    NPdataset = on_data()
    
    plotter(NPdataset)
    
    
    
    
    