#!/usr/bin/env python
# coding: utf-8

# # For real time streaming of accounts. ONLY RUN

# In[1]:


import tweepy 
import json

#Importing twitter credentials
# from twitter_credentials import *


# In[2]:


#Accesing twitter from the App created in my account
def autorize_twitter_api():
    consumer_key = "jzn0NU9EviCRRbONbUXX9a8VN"
    consumer_secret = "ULsKu9BjBPmZ3yY5NdS6EXUhGBNWKUWxtwKqFktBeqsOq1Y3ZQ"
    access_token = "781482721-6928Gtnj95bK82PW3fYDxHFvU5T4l3SPI4VVF1X2"
    access_token_secret = "fTxclLJ4oxEmqshRhSbBibGoUiNq1l6941C0VyREdTf41"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    return auth


# In[3]:


class MyStreamListener(tweepy.StreamListener):
    
    """
    def on_status(self, status):
        print(status.text)
    """
    def __init__(self, filename, api=None):
        self.filename = filename
    
        tweepy.StreamListener.__init__(self, api=api)

        
    def on_data(self, raw_data):

        try:
            with open(self.filename, 'a') as file:
                file.write(raw_data)
  
            
        except Exception as e:
            print(e)
    
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False


# In[4]:


# For realtime streaming
if __name__ == "__main__": 
    #Creates the table for storing the tweets
    term_to_search = input("Enter hashtag to see live results: ")
    
    #Connect to the streaming twitter API
    api = tweepy.API(wait_on_rate_limit_notify=True)
    
    #Stream the tweets
    streamer = tweepy.Stream(auth=autorize_twitter_api(), listener=MyStreamListener(api=api, filename='tweets.txt'))
    streamer.filter(languages=["en"], track=[term_to_search])   
    myStream.disconnect()


# In[ ]:




