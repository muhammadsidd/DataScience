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
#loc looks at location by row. 
print(df.loc[1, 'Country'])

############## value counts gives the count of the columns by adding all the records (rows) ###########
print(df['Country'].value_counts())

df2= df['Country'].value_counts()

# df2.to_csv('pakistan.csv')

# print("RIP\n")

#aggregated value of a specific column with filter
print(df.loc[df['Country']=='Pakistan'].agg(['count']))

# print("RIP\n")
countries = ['United States','Pakistan','United Kingdom','Canada']
#filter high salary this will return a boolean series 
high_sal = ((df['ConvertedComp'] >= 70000) & (df['Country'].isin(countries)) & (df['LanguageWorkedWith'].str.contains('Python', na = False)))
#pass the boolean series to df.loc[filter,[spcify columns u wish to have in this df, if nothing is chosen all columns will be displayed]]
print(df.loc[high_sal,['Country', 'LanguageWorkedWith']])
schema_df.sort_index()
# print(schema_df.head(10))

for column in df['Country'].unique():
    print(column)

print([x.upper() for x in df.columns])

# df.columns = [x.upper() for x in df.columns]

#will change spaces in column names to _ 
df.columns = df.columns.str.replace(' ','_')

print(df.loc[2,'LanguageWorkedWith'])
print(df.head())

df.loc[2,['Country','LanguageWorkedWith']] = ['Russia', 'Python']
print(df.loc[2,['Country','LanguageWorkedWith']])

df.Country = df.Country.str.lower()## convert this column values in to lower case
print(df.loc[2,['Country']]) 

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

################################################################   GROUP BY  #################################################################################################
## group by returns a groupby type which is iterable, the index of this is based on what the user has specified the groupby on in the following example we will groupby 'Country'

print("\n\n\n\n\n HERE NOW")
for cols in df.columns:
    print(cols)

print(df['SalaryUSD'].count())

print(df['Hobbyist'].value_counts())
print(df['SocialMedia'].value_counts(normalize=True)) #percentage instead of raw numbers use normalize = true

#groupby means operation that inolves some combination of splitting the object and applying a funtion to combine the result 
print(df["Country"].value_counts())

country_group = df.groupby(['Country'])
print(type(country_group)) #groupby object
print(country_group.get_group('united states')['SocialMedia'].value_counts()) #u can set normalize = True inside value counts for %
print(country_group['SocialMedia'].value_counts())

#### Number of people who know python in each country by percentage -- QUIZ 

#--- PREVIOUS APROACH -- #
# language_group = df.groupby(['LanguageWorkedWith'])
# print("QUIZZZZZ ANSWERRRRRR\n\n\n")
# print(language_group.get_group('Python')['Country'].value_counts(normalize=True))

#apply wil apply this lambda funtion to each cell, since each cell (now x in lambda) is a series we can apply the str.contains method which was forbidden on groupbyseries type
knows_python = country_group['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum()) #number of people in each country who know python
country_res = df['Country'].value_counts() #Total number of people within each country 
python_df =   pd.concat([country_res,knows_python], axis ='columns', sort=False)    #using concat to merge the two series together fo further calculations 
print("\n\n\n PYTHON DF % \n\n\n")
python_df.rename(columns={'Country':'NumResp','LanguageWorkedWith':'NumKnowsPython'},inplace=True)
python_df['PCTknowsPython'] =  (python_df['NumKnowsPython']/python_df['NumResp']) * 100
#sort by highest %knows python first, df will be sorted in descending order. 
python_df.sort_values(by='PCTknowsPython',ascending=False, inplace=True)
print(python_df)
print(python_df.loc['japan'])

print(country_group.get_group('united states')['SalaryUSD'].median())
print(country_group['SalaryUSD'].median().loc['united states'])
##aggrigate function call takes arguments as a list type see example as follows 
print(country_group['SalaryUSD'].agg(['median','mean']).loc['united states'])



#alternatively we can use filter for just one group like so 
filt = df['Country'] == 'united states'
tempdf = df.loc[filt]
print('\nPEOPLE WHO KNOW PYTHON IN USA \n\n\n\n\n')
print(tempdf['SocialMedia'].value_counts())
print(tempdf['LanguageWorkedWith'].str.contains('Python').sum())

#or







