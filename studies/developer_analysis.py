import pandas as pd
from collections import Counter
df = pd.read_csv('developerdata.csv', index_col='Respondent')
# print (df.shape)
# print (df.info())

schema_df = pd.read_csv('developerschema.csv')

pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)

print(df.head(5))
# print(schema_df)

########## to refer to a column in df u can simple use ###

print(df[df['Country'] == 'Pakistan'].count())
print(df.loc[1, 'Country'])
print(df['Country'].value_counts())

schema_df.sort_index()
print(schema_df.head())