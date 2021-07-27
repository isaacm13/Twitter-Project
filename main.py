#!/usr/bin/env python
# coding: utf-8

# # Mining Twitter Data for Sentiment Analysis

# Sentiment Analysis using tweepy
# 
# Using OAuth to pull Twitter's data via their API

# In[1]:


import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'YOUR-CONSUMER-KEY'
consumer_secret = 'YOUR-CONSUMER-SECRET'
access_token = 'YOUR-ACCESS-TOKEN'
access_secret = 'YOUR-ACCESS-SECRET'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)



# Collecting tweets in json file in regards to file "User Input Hashtag Live Stream-Tweet"

# In[2]:


class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)


# ### Sample attributes of types of data pulled from tweets

# text: the text of the tweet itself
# 
# created_at: the date of creation
# 
# favorite_count, retweet_count: the number of favourites and retweets
# 
# favorited, retweeted: boolean stating whether the authenticated user (you) have favourited or retweeted this tweet
# 
# lang: acronym for the language (e.g. “en” for english)
# 
# id: the tweet identifier
# 
# place, coordinates, geo: geo-location information if available
# 
# user: the author’s full profile
# 
# entities: list of entities like URLs, @-mentions, hashtags and symbols
# 
# in_reply_to_user_id: user identifier if the tweet is a reply to a specific user
# 
# in_reply_to_status_id: status identifier id the tweet is a reply to a specific status
# 
# Processing tweets
# Tokenizing the tweet
# Tokenizing @-mentions, emoticons, URLs and #hash-tags as individual tokens.

# Sentiment Analysis refers to the process of taking natural language to identify and extract subjective information. 
# You can take text, run it through the TextBlob and the program will spit out if the text is positive, neutral, or negative by analyzing the language used in the text.

# To calculate the overall sentiment, we look at the polarity score:
# 
# Positive – from .01 to 1
# Neutral – 0
# Negative – from –.01 to -1
