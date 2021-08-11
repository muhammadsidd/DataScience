import pandas as pd
from collections import Counter
df = pd.read_csv('developerdata.csv', index_col='Respondent')
# print (df.shape)
# print (df.info())

schema_df = pd.read_csv('developerschema.csv', index_col='Column')

pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)

# print(df.head(5))
# print(schema_df)

######### to refer to a column in df u can simple use ###
#### could also use '|' and '&' in the filter of the df. 
# print(df[df['Country'] == 'Pakistan'])
# print(df[df['Country'] == 'Pakistan'].count())
# print("\nTHIS IS COUNTRY\n")

########## first record's location #####################
# print(df.loc[1, 'Country'])

############## value counts gives the count of the columns by adding all the records (rows) ###########
# print(df['Country'].value_counts())

df2= df['Country'].value_counts()

# df2.to_csv('pakistan.csv')

# print("RIP\n")

# print(df.loc[df['Country']=='Pakistan'].agg(['count']))

# print("RIP\n")
countries = ['United States','Pakistan','United Kingdom','Canada']
high_sal = ((df['ConvertedComp'] >= 70000) & (df['Country'].isin(countries)) & (df['LanguageWorkedWith'].str.contains('Python', na = False)))
# print(df.loc[high_sal,['Country', 'LanguageWorkedWith']])
schema_df.sort_index()
# print(schema_df.head(10))

# for column in df['Country'].unique():
#     print(column)

# print([x.upper() for x in df.columns])

# df.columns = [x.upper() for x in df.columns]

#will change spaces in column names to _ 
df.columns = df.columns.str.replace(' ','_')

# print(df.loc[2,'LanguageWorkedWith'])
# print(df.head())

df.loc[2,['Country','LanguageWorkedWith']] = ['Russia', 'Python']
# print(df.loc[2,['Country','LanguageWorkedWith']])

df.Country = df.Country.str.lower()## convert this column values in to lower case
# print(df.loc[2,['Country']]) 

### APPLY #####

## you can pass in the entire column to any function, in other words you can apply every function to each record of the column 
df['Country'] = df['Country'].astype(str) #convert data into into 
print(df['Country'].apply(lambda x: x.lower())) #apply length function to it (upper function is just as example, it could be a custom function/ user defined / lambda)

# for apply functions on individual elements of dataframe instead of series (column) of dataframe use applymap
df.astype(str)
df.applymap(lambda x : len)
df['LanguageWorkedWith'] = df['LanguageWorkedWith'].replace({'Python': 'Python3'})

print(df.loc[high_sal,['LanguageWorkedWith']])
df.rename(columns={'ConvertedComp':'SalaryUSD'}, inplace=True)
print(df.loc[high_sal,['SalaryUSD']])

df['Hobbyist'] = df['Hobbyist'].map({"Yes":True, "No":False}) ## use replace instead of map if you DONOT wanna convert values like not sure or others to nan. 

print(df.head())