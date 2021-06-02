import tweepy as tw
import nltk 
from nltk.corpus import stopwords
from textblob import Word, TextBlob
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from IPython.display import display

nltk.download('stopwords')
nltk.download('wordnet')
stop_words = stopwords.words('english')
custom_stopwords = ['rt' , '$amc']

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

######################### QUERY ############################

hashtag = '$AMC'
query = tw.Cursor(api.search, q=hashtag).items(1000)
#tweet.from_user
tweets = [{'Tweets':tweet.text, 'Timestamp':tweet.created_at} for tweet in query]
print(tweets)

df = pd.DataFrame.from_dict(tweets)
print(df.head())
print(df.shape)

buy_refs = ['buy','moon','hold','call','suits','rich','diamond','load','win','all in', 'investing']
sell_refs = ['crash','sell','careful','profits','halt','put', 'bear','bull','short','lose', 'ban']

def identify_subject(tweet,refs):
    flag =0
    for ref in refs:
        if tweet.find(ref) != -1:
            flag =1
    return flag

df['Buy'] = df['Tweets'].apply(lambda x: identify_subject(x.lower(),buy_refs))
df['Sell'] = df['Tweets'].apply(lambda x: identify_subject(x.lower(),sell_refs))

print("\n")
print(len(df[df['Buy']== 1])," Buy references")
print(len(df[df['Sell']== 1]), "Sell references")

######################### PREPROCESS ########################

def preprocess_tweets(tweet, custom_stopwords):
    preprocess_tweet = tweet
    preprocess_tweet.replace('[^\w\s]','')
    preprocess_tweet = " ".join(word for word in preprocess_tweet.split() if word not in stop_words)
    preprocess_tweet = " ".join(word for word in preprocess_tweet.split() if word not in custom_stopwords)
    preprocess_tweet = " ".join(Word(word).lemmatize() for word in preprocess_tweet.split())

    return preprocess_tweet

df['Processed Tweet'] = df['Tweets'].apply(lambda x: preprocess_tweets(x.lower(), custom_stopwords))



####################### SENTIMENTAL ANALYSIS ###################

df['polarity'] = df['Processed Tweet'].apply(lambda x: TextBlob(x).sentiment[0])
df['subjectivity'] = df['Processed Tweet'].apply(lambda x: TextBlob(x).sentiment[1])

##BUYING SENTIMENT
##filtering out the data where buying is set to 1 and only returning buy, polarity and subjectivity coloumns and grouping it by buy coloumns 
## while applying aggrate function to it. 
display(df[df['Buy']==1][['Buy','polarity','subjectivity']].groupby('Buy').agg([np.mean, np.max, np.min, np.median]))

##SELLING SENTIMENT
##filtering out the data where selling is set to 1 and only returning sell, polarity and subjectivity coloumns and grouping it by sell coloumns 
## while applying aggrate function to it. 
display(df[df['Sell']==1][['Sell','polarity','subjectivity']].groupby('Sell').agg([np.mean, np.max, np.min, np.median]))

print(df.head())

########################## DATA VISUALIZATION ##################

buy = df[df['Sell']==1][['Timestamp','polarity']]
buy = buy.sort_values(by='Timestamp',ascending=True)
buy['MA Polarity'] = buy.polarity.rolling(10, min_periods=3).mean()

sell = df[df['Sell']==1][['Timestamp','polarity']]
sell = sell.sort_values(by='Timestamp',ascending=True)
sell['MA Polarity'] = sell.polarity.rolling(10, min_periods=3).mean()

sellers = 'red'
buyers = 'blue'
fig, axes = plt.subplots(2, 1, figsize=(13, 10))

axes[0].plot(sell['Timestamp'], sell['MA Polarity'],color = sellers)
axes[0].set_title("\n".join(["Selling Polarity"]))
axes[1].plot(buy['Timestamp'], buy['MA Polarity'], color=buyers)
axes[1].set_title("\n".join(["Buying Polarity"]))

fig.suptitle("\n".join(["AMC Rally Analysis"]), y=0.98)

plt.show()