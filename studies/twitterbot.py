import tweepy
import time
import json
import nltk
from nltk.corpus import stopwords
import pandas as pd
from textblob import Word, TextBlob
import random

consumer_key = ''
consumer_secret = ''
key = ''
secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
#api.update_status('Twitter bot reporting in live ')

user = "elonmusk"
num = 100
FILE_NAME = 'last_seen.txt'
tweetlist = []
userlist = []
ids = []
# tweet = api.mentions_timeline()[0]
# print(json.dumps(tweet._json, indent=2))
# print(tweet.user.screen_name)

def readlastseen(FILE_NAME):
    file_read = open(FILE_NAME,'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def writelastseen(FILE_NAME, last):
    file_write = open(FILE_NAME,'w')
    file_write.write(str(last))
    file_write.close()
    return

def collect():
    tweets = api.mentions_timeline(readlastseen(FILE_NAME))
    for tweet in reversed(tweets):
        tweetlist.append(tweet.text)
        userlist.append(tweet.user.screen_name)
        ids.append(tweet.id)
        print(str(tweet.id)+'--'+tweet.text)
        
        # writelastseen(FILE_NAME, tweet.id)

df = pd.DataFrame({'id':ids,'userlist':userlist,'tweets':tweetlist})

# Create stopword list:
nltk.download('stopwords')
nltk.download('wordnet')
stop_words = stopwords.words('english')
custom_stopwords = ["br", "href"]

def preprocess_tweets(tweet, custom_stopwords):
    preprocess_tweet = tweet
    preprocess_tweet.replace('[^\w\s]','')
    preprocess_tweet = " ".join(word for word in preprocess_tweet.split() if word not in stop_words)
    preprocess_tweet = " ".join(word for word in preprocess_tweet.split() if word not in custom_stopwords)
    preprocess_tweet = " ".join(Word(word).lemmatize() for word in preprocess_tweet.split())

    return preprocess_tweet

df['Processed Tweet'] = df['tweets'].apply(lambda x: preprocess_tweets(x.lower(), custom_stopwords))
df['polarity'] = df['Processed Tweet'].apply(lambda x: TextBlob(x).sentiment[0])
df['subjectivity'] = df['Processed Tweet'].apply(lambda x: TextBlob(x).sentiment[1])

def sarcasticline():
    lines = open('sarcasm.txt').read().splitlines()
    return random.choice(lines)


def actions():
    api.update_status("@" + tweet.user.screen_name + sarcasticline(), tweet.id)
    api.create_favorite(tweet.id)
    api.retweet(tweet.id)
    

def search(name,numberoftweets):
    tweets = tweepy.Cursor(api.user_timeline, name).items(numberoftweets)
    for tweet in tweets:
        try:
            tweet.retweet()
            print("DONE RETWEETING " + tweet.text)
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

# while True:
#     reply()
#     search(user,num)

print(df)

