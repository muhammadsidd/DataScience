import requests
import json
import pandas as pd
import numpy as np
from pprint import pprint
import random
# from bs4 import BeautifulSoup
from urllib.request import urlopen
import unicodedata
import re

url = "https://en.wikipedia.org/wiki/List_of_romantic_comedy_films"

tables = pd.read_html(url)
romcom_df = pd.concat(tables,sort=False)
print(tables[1])

# 
romcom_df.columns = ["Year","Title","Director","Country","Notes","Empty", "NA", "NA2"]
romcom_df = romcom_df.filter(items=["Year","Title","Director","Country"])
romcom_df = romcom_df.set_index("Country")
romcom_df = romcom_df.filter(like='United States', axis= 0)
romcom_df = romcom_df.reset_index()
romcom_df = romcom_df.filter(items=["Year","Title"])
romcom_df.to_csv('romcom2.csv')