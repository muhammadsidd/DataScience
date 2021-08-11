import pandas as pd
from collections import Counter
df = pd.read_csv('developerdata.csv', index_col='Respondent')
print (df.shape)
print (df.info())

schema_df = pd.read_csv('developerschema.csv', index_col='Column')

pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)

print(df.head(5))
print(schema_df)

######### to refer to a column in df u can simple use ###
#### could also use '|' and '&' in the filter of the df. 
print(df[df['Country'] == 'Pakistan'])
print(df[df['Country'] == 'Pakistan'].count())
print("\nTHIS IS COUNTRY\n")

########## first record's location #####################
print(df.loc[1, 'Country'])

############## value counts gives the count of the columns by adding all the records (rows) ###########
print(df['Country'].value_counts())

df2= df['Country'].value_counts()

# df2.to_csv('pakistan.csv')

print("RIP\n")

print(df.loc[df['Country']=='Pakistan'].agg(['count']))

print("RIP\n")
countries = ['United States','Pakistan','United Kingdom','Canada']
high_sal = ((df['ConvertedComp'] >= 70000) & (df['Country'].isin(countries)) & (df['LanguageWorkedWith'].str.contains('Python', na = False)))
print(df.loc[high_sal,['Country', 'LanguageWorkedWith']])
schema_df.sort_index()
print(schema_df.head(10))