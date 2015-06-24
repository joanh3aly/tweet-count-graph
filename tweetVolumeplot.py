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


def dataProcess(hourArray,CSVdata,hourNumber):
    hourArray = []
         
    for index in range(len(CSVdata)):
        if(CSVdata[index][1] == hourNumber):
            hourArray.append(CSVdata[index][1])
                     
    # Count amount of records in Numpy array
    tweetCount = len(hourArray) 
    # Find the hour recorded (by retrieving first record in array)      
    hourRecorded= hourArray[0]
    
    return (hourRecorded, tweetCount)

  
# this function counts how many tweets with defined subject matter/user id are tweeted per hour, returns a numpy array
def read_data():	
	# Create a numpy array from CSV data file - splits at tab   
    CSV_data = genfromtxt('/Applications/MAMP/htdocs/social_test/twitter/network-map/station-tweet-data/cj3-20150611-18.data', delimiter='\t',autostrip=True)
    
    #run the hourly data processing script
    hourRecorded1, tweetCount1 = dataProcess("one",CSV_data,1)
    hourRecorded2, tweetCount2 = dataProcess("two",CSV_data,2) 
    hourRecorded3, tweetCount3 = dataProcess("three",CSV_data,3)
    hourRecorded4, tweetCount4 = dataProcess("four",CSV_data,4) 
    hourRecorded5, tweetCount5 = dataProcess("five",CSV_data,5)
    hourRecorded6, tweetCount6 = dataProcess("six",CSV_data,6) 
    hourRecorded7, tweetCount7 = dataProcess("seven",CSV_data,7)
    hourRecorded8, tweetCount8 = dataProcess("eight",CSV_data,8) 
    hourRecorded9, tweetCount9 = dataProcess("nine",CSV_data,9)
    hourRecorded10, tweetCount10 = dataProcess("ten",CSV_data,10) 
    hourRecorded11, tweetCount11 = dataProcess("eleven",CSV_data,11)
    hourRecorded12, tweetCount12 = dataProcess("twelve",CSV_data,12) 
    hourRecorded13, tweetCount13 = dataProcess("thirteen",CSV_data,13)
    hourRecorded14, tweetCount14 = dataProcess("fourteen",CSV_data,14) 
    hourRecorded15, tweetCount15 = dataProcess("fifteen",CSV_data,15)
    hourRecorded16, tweetCount16 = dataProcess("sixteen",CSV_data,16) 
    hourRecorded17, tweetCount17 = dataProcess("seventeen",CSV_data,17)
    hourRecorded18, tweetCount18 = dataProcess("eighteen",CSV_data,18) 
    hourRecorded19, tweetCount19 = dataProcess("nineteen",CSV_data,19)
    hourRecorded20, tweetCount20 = dataProcess("twenty",CSV_data,20) 
    hourRecorded21, tweetCount21 = dataProcess("twentyone",CSV_data,21)
    hourRecorded22, tweetCount22 = dataProcess("twentytwo",CSV_data,22) 
    hourRecorded23, tweetCount23 = dataProcess("twentythree",CSV_data,23)
    hourRecorded24, tweetCount24 = dataProcess("twentyfour",CSV_data,24) 
      
    # Create new NP array with hour and number of tweets
    hourlyTweetNo = np.array([[hourRecorded1, tweetCount1],[hourRecorded2, tweetCount2],[hourRecorded3, tweetCount3],[hourRecorded4, tweetCount4],[hourRecorded5, tweetCount5],[hourRecorded6, tweetCount6],[hourRecorded7, tweetCount7],[hourRecorded8, tweetCount8],[hourRecorded9, tweetCount9],[hourRecorded10, tweetCount10],[hourRecorded11, tweetCount11],[hourRecorded12, tweetCount12],[hourRecorded13, tweetCount13],[hourRecorded14, tweetCount14],[hourRecorded15, tweetCount15],[hourRecorded16, tweetCount16],[hourRecorded17, tweetCount17],[hourRecorded18, tweetCount18],[hourRecorded19, tweetCount19],[hourRecorded20, tweetCount20],[hourRecorded21, tweetCount21],[hourRecorded22, tweetCount22],[hourRecorded23, tweetCount23],[hourRecorded24, tweetCount24]])
  
    hourlyTweetNo = np.array([[hourRecorded18, tweetCount18],[hourRecorded19, tweetCount19]])
    
    return hourlyTweetNo
    
    
def plotter(NPtweetsperhour):
    # Finally, plot the data!    
    plt.plot(NPtweetsperhour[[1]],NPtweetsperhour[[0]], 'ro')
    plt.axis([0, 24, 0, 200])
    plt.xlabel('hour', fontsize=18)
    plt.ylabel('tweet-volume', fontsize=18)
    plt.show()
    
    # to save the figure to a file
    plt.savefig('/Applications/MAMP/htdocs/social_test/twitter/network-map/out.png')   	
    
    return True

    
# run code in main file not from another module
if __name__ == '__main__':  
    
    NPdataset = read_data()
    
    plotter(NPdataset)
    
    # Next: experiment with running the script every day?
    #  threading.Timer(60, f).start()
    
    
    
    
    