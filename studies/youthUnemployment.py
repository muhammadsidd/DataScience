import pandas as pd
import numpy as np
import matplotlib as plt
from matplotlib import style

style.use('fivethirtyeight')

country= pd.read_csv('E:\\SummitWorks_training\\DataScience\\youth_unemployment.csv', index_col=0)

df = country.head(5)
df = df.set_index(["Country Code"])
##sd = df.reindex(columns = ['2010','2011']) 
db = df.diff(axis=1) ## percentage change between 2010 to 2011

db.plot(kind = 'bar')
plt.pyplot.plot(kind = 'bar')
plt.pyplot.show()

print(df.describe())

print(df.sum())
print(df.max(axis=1))
