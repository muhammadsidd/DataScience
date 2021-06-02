import tweepy as tw
import nltk 
import matplotlib as plt
import pandas as pd
import numpy as np

################# TWITTER API CREDENTIALS ####################
consumer_key = "ENRr83l2o7OS8y4DJdoFWhrpj"
consumer_secret = "oeGcJlnmMSitq2qX2UoyJpcXQZMwu2DyHLpNGJSH6KGIRsUZAz"
bearer_Token = "AAAAAAAAAAAAAAAAAAAAAHZYKwEAAAAAzbhJPlPgVUU1kuCvuYP9hTg2%2BTs%3DIVX5YuFJvJJBFhH467eagnUMcnoQTrE1kYO9szbaqu1IFWcZX0"
access_token = "1340798338497703937-2X0cwWG6tua9OyJdZTMNRLRnoP19gr"
access_token_secret = "8rEjjTmqFxVFD4fCOdVwaNZTkAaFZUwYkEWhYZo7WnzFt"
##############################################################

################### AUTHENTICATION ##########################
auth = tw.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tw.API(auth,wait_on_rate_limit=True)
############################################################

######################### QUERY ############################

hashtag = '#presidentialdebate'
query = tw.Cursor(api.search, q=hashtag).items(1000)
#tweet.from_user
tweets = [{'Tweets':tweet.text, 'Timestamp':tweet.created_at} for tweet in query]
print(tweets)