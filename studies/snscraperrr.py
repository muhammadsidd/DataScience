import pandas as pd
from tqdm.notebook import tqdm
import snscrape.modules.twitter as sntwitter

scraper = sntwitter.TwitterSearchScraper("#python")

for tweet in scraper.get_items():
    print(tweet)
    break