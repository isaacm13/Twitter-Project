#!/usr/bin/env python
# coding: utf-8

# In[25]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install matplotlib')


# In[2]:


get_ipython().system('pip install tweepy ')


# In[26]:


import tweepy #used to work with Twitter's API
import webbrowser
import time
import pandas as pd
import datetime 
import numpy as np
import matplotlib.pyplot as plt
import re
import json


# In[27]:


consumer_key = "jzn0NU9EviCRRbONbUXX9a8VN" #pulled from developer account for Twitter
consumer_secret = "ULsKu9BjBPmZ3yY5NdS6EXUhGBNWKUWxtwKqFktBeqsOq1Y3ZQ" #pulled from developer account for Twitter
#key and secret is generated by Twitter developer account


# In[28]:


callback_uri = 'oob'#url 


# In[29]:


auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri) #authorization to pull data from Twitter's API
redirect_url = auth.get_authorization_url() 
print(redirect_url)


# In[30]:


webbrowser.open(redirect_url)


# In[31]:


user_pint_input = input("What's the pin value? ") #this is based upon Twitter Developer account
#Pin is generated new everytime this cell is run


# In[32]:


auth.get_access_token(user_pint_input)


# In[33]:


print(auth.access_token, auth.access_token_secret)


# In[34]:


api = tweepy.API(auth)


# In[35]:


def extract_timeline_as_df(timeline_list):
    columns = set()
    allowed_types = [str, int]
    tweets_data = []
    for status in timeline_list:
        status_dict = dict(vars(status))
        keys = status_dict.keys()
        single_tweet_data = {"user": status.user.screen_name, "author": status.author.screen_name}
        for k in keys:
            try:
                v_type = type(status_dict[k])
            except:
                v_type = None
            if v_type != None:
                if v_type in allowed_types:
                    single_tweet_data[k] = status_dict[k]
                    columns.add(k)
        tweets_data.append(single_tweet_data)


    header_cols = list(columns)
    header_cols.append("user")
    header_cols.append('author')
    df = pd.DataFrame(tweets_data, columns=header_cols)
    return df


# In[37]:


# pulls data from Visual Studio Code's twitter page https://twitter.com/code
screen_name = "code"
#user = api.get_user(screen_name)
#user_timeline = user.timeline(screen_name)  # recent tweets are pulled in the spreadsheet
#print(user_timeline) 
# fetching the statuses
user_timeline = api.user_timeline(screen_name, count=200)#tweet count limit is 200
df1 = extract_timeline_as_df(user_timeline)
print(df1)


# In[23]:


screen_name = "code" #pulls data from Visual Studio Code's twitter page https://twitter.com/code
user = api.get_user(screen_name)
user_timeline = user.timeline() 
df1 = extract_timeline_as_df(user_timeline) #recent tweets are pulled in the spreadsheet
df1.head(201)


# In[16]:


df1.to_csv('tweetspreadsheet.csv', index=False)


# In[17]:


df1_saved_file = pd.read_csv('tweetspreadsheet.csv')
df1_saved_file


# In[18]:


# screen name of the account to be fetched
screen_name = "code"
  
# number of statuses to be fetched
count = 3
  
# fetching the statuses
statuses = api.user_timeline(screen_name, count = count)
  
# printing the statuses
for status in statuses:
    print(status.text, end = "\n\n")


# In[19]:


#search_words = ["#covid19", "2020", "lockdown"]
key_word = '@code' #searches all tweets that reference the key_word specified 
date_since = "2021-06-21"

tweets = tweepy.Cursor(api.search, key_word, geocode="38.892062,-77.019912,3000km", lang="en", since=date_since).items(10)
## the geocode is for Washington, DC; format for geocode="lattitude,longitude,radius"
## radius should be in miles or km
#items references the number of tweets to pull 


for tweet in tweets:
    print("created_at: {}\nuser: {}\ntweet text: {}\ngeo_location: {}".
            format(tweet.created_at, tweet.user.screen_name, tweet.text, tweet.user.location))
    print("\n")
## tweet.user.location will give you the general location of the user and not the particular location for the tweet itself, as it turns out, most of the users do not share the exact location of the tweet


# In[20]:


date_since = '2021-06-14'
date_until = '2021-06-21'
tweets = tweepy.Cursor(api.search,q='test', since=date_since,until=date_until).items(10)
for tweet in tweets:         
    print (tweet.text)  


# In[21]:


for status in tweepy.Cursor(api.user_timeline, screen_name='@code', tweet_mode="extended").items():
    print(status.full_text)


# In[22]:


comp_searches = ("@code")
# Array to hold sentiment
sentiments = []
# Iterate through all the comp_searches
for search in comp_searches:
       
    # Bring out the 100 tweets
    comp_tweets = api.user_timeline(search, count=100)
    
    # Loop through the 100 tweets
    for tweet in comp_tweets:
        text = tweet["text"]
        
     # Add each value to the appropriate array
        sentiments.append({"User": search,"text":text,"Date": tweet["created_at"]})


# In[ ]:




