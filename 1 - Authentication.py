#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tweepy
import webbrowser
import time


# In[4]:


consumer_key = "jzn0NU9EviCRRbONbUXX9a8VN"
consumer_secret = "ULsKu9BjBPmZ3yY5NdS6EXUhGBNWKUWxtwKqFktBeqsOq1Y3ZQ"


# In[5]:


callback_uri = 'oob'#url 


# In[7]:


auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
redirect_url = auth.get_authorization_url() 
print(redirect_url)


# In[9]:


webbrowser.open(redirect_url)


# In[ ]:





# In[13]:


user_pint_input = input("What's the pin value? ")


# In[15]:


auth.get_access_token(user_pint_input)


# In[16]:


print(auth.access_token, auth.access_token_secret)


# In[17]:


api = tweepy.API(auth)


# In[18]:


me = api.me()


# In[19]:


print(me.screen_name)


# In[ ]:




