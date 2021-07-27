#!/usr/bin/env python
# coding: utf-8

# This creates a csv file of the entered hashtag by the user and populates data from recently pull tweets based on the number to pull by the user.
# Check the folder of the name of the hashtag with .csv to see the results. 

# In[1]:


# importing required libraries
import tweepy
import csv
import datetime
import time


# In[2]:


#define and store your credintials

consumer_key = "jzn0NU9EviCRRbONbUXX9a8VN"
consumer_secret = "ULsKu9BjBPmZ3yY5NdS6EXUhGBNWKUWxtwKqFktBeqsOq1Y3ZQ"
access_token = "781482721-6928Gtnj95bK82PW3fYDxHFvU5T4l3SPI4VVF1X2"
access_token_secret = "fTxclLJ4oxEmqshRhSbBibGoUiNq1l6941C0VyREdTf41"

#Tweepy auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# In[3]:


#Enter the keyword (kw) that you want to collect tweets based on it
kw = input('Enter keyword: ')


# In[4]:


#Enter the number of the tweets you want to fetch
num = int(input('Number of tweet (enter -1 if you want max number) : '))


# In[5]:


# Open/Create a file to append data
csvFile = open(kw+'.csv', 'w+')


# In[6]:


#Use csv Writer
csvWriter = csv.writer(csvFile)


# In[7]:


#Columns that you want to print in CSV file
csvWriter.writerow(['Tweet_Date', 'user_id','Followers','Tweet_text'])


# In[8]:



apicalls = 0
counter =0


# In[9]:


for tweet in tweepy.Cursor(api.search,q=kw,count=100).items():
    
    apicalls = apicalls+1
    if (apicalls == 150*100):
        print("sleep")
        apicalls = 0
        time.sleep(15*60)
    
    
    csvWriter.writerow([tweet.created_at, tweet.user.screen_name, tweet.user.followers_count, tweet.text.encode('utf-8')])
    counter=counter+1
    
    if num==-1:
        pass
    elif counter==num:
        break
        
csvFile.close()
print("Fetch Finished")


# In[ ]:




