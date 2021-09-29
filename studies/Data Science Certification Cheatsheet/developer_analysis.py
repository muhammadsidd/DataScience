from os import replace
import pandas as pd
import numpy as np
from collections import Counter
from pandas.core.frame import DataFrame
from pandas.core.indexes.base import Index
from pandas.io.parsers import read_csv
import sqlalchemy
import pymysql
import matplotlib as plt
from matplotlib import style
style.use("fivethirtyeight")


record1 = pd.DataFrame({
    "Day":[1,2,3,4,5,6,7],
    "Seeders": [25,51,97,50,23,52,17],
    "Click" : [22,115,14,51,13,42,51]
}, index= ['a','b','c','d','e','f','g'])

record2 = {
    "Downloads":[1,2,3,4,5,6,7],
    "Uploads": [1000,500,100,50,25,5,1],
    "watched" : [25,15,10,5,3,2,1]
}


df = pd.DataFrame(record2, index= ['a','b','c','d','e','f','g'])
print(df) ##only 3 rows
print(df.tail(2)) #last 2
## mer = pd.merge(df,record1, on="Day") //will merge on the key. SHOULD HAVE SAME KEY for on = 

joined = df.join(record1) #join the two using the same index. 
print(joined)

 ##### Make one key your index / primary key ########
df.set_index("Downloads", inplace=True) #inplace = True will permanently change ur dataframe 
df.plot()

##Change colomn headers ##
df = df.rename(columns={"watched":"Users"})
print(df)

concate = pd.concat([df,record1]) #going to default to num index if same index for first dataset and second dataset
print(concate)

###DATA MUNGING#######

country = pd.read_csv('C:\\Users\\Talha\\Downloads\\data_csv.csv')
c5 = country.head(5)
print(c5)
print(c5[c5["Real Price"] > 90]) 

c5.to_html('great_snp.html')

############# CLEANING DATA #########################
data = c5.dropna(axis='index', how='any', subset=['Real Dividend','PE10'])
data= c5.replace('NA', np.nan)
print(data.isna())
data.fillna(0, inplace=True)
print(data)
    #any = drop the record index(row) if any value is missing
    #all = delete the record if and only if all values are missing 
    #axis = 'index' for rows 'coloumns' for columns
    #subset = list of column(s) that are compulsary if the record has this missing column the record will be dropped entirely
    # if there are two values then it will show atleast one which is filled and not delete the record. 
print(data.dtypes)

############################Conversion ##############################
data['PE10'] = data['PE10'].astype(int)
print(data['SP500'].mean())


df = pd.read_csv('developerdata.csv', index_col='Respondent')
print (df.shape)
print (df.info())

schema_df = pd.read_csv('developerschema.csv', index_col='Column')

pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)
print(df.columns.values)
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
print('\n\nProgrammers using SOCIAL MEDIA IN THE USA \n',country_group.get_group('united states')['SocialMedia'].value_counts()) #u can set normalize = True inside value counts for %
print('\n\nSHOW ME NOWWWW \n',country_group['SocialMedia'].value_counts())

#### Number of people who know python in each country by percentage -- QUIZ 

#--- PREVIOUS APROACH -- #
# language_group = df.groupby(['LanguageWorkedWith'])
# print("QUIZZZZZ ANSWERRRRRR\n\n\n")
# print(language_group.get_group('Python')['Country'].value_counts(normalize=True))

#apply wil apply this lambda funtion to each cell, since each cell (now x in lambda) is a series we can apply the str.contains method which was forbidden on groupbyseries type
knows_python = country_group['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum()) #number of people in each country who know python return type = series 
country_res = df['Country'].value_counts() #Total number of people within each country in series 
python_df =   pd.concat([country_res,knows_python], axis ='columns', sort=False)    #using concat to merge the two series together fo further calculations 

print("\n\n\n Country RESpondants\n", type(country_res))
print("\n\n\n Country know Python\n", type(knows_python))


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

print(df.columns.values)

############################## READING/Writing DATA FROM SQL AND SAVING TO SQL ################

engine = sqlalchemy.create_engine("mysql+pymysql://root:Mostwanted1996*@localhost:3306/demodb")
sql_table = pd.read_sql_table("person",engine, columns=['name']) #remove column = name to print entire table 
print(sql_table)
query = "some query"
pd.read_sql_query(query, engine) # can take argumnets for chunks read documentation
## alternatively u can use pd.read_sql

##### saving into sql table 

df = pd.read_csv("some file") #need to have same column names as db table 
df.to_sql(name = 'person',con = engine, index=False, if_exists= np.append ) #if_exists has other options, consider reading the documentation 

################################# JOINS/MERGES ##########################################

df = DataFrame({"city":['chicago','NYC','sanfrancisco'], "humidity":[55,54,56]})
df2 =DataFrame({"city":['chicago','NYC','Tampa'], "temp":[85,84,96]})

df3 = pd.merge(df,df2, on="city",how="outer", indicator=True)
#### HOW #####
#outer is union of the two dataframe 
#inner is intersection that means only common cities in 2 fds 
#left is gonna give u the whole of df1 and intersection
#right is gonna give u the whole of df2 and intersection 
#### INDICATOR = True #####
#shows were data came from, left or right 
print(df3)



############################# in chunks ###################
chunk_size =  5000
batch_no = 1

for chunk in pd.read_csv('movie_rating.csv',chunksize=chunk_size):
    chunk.to_csv('movie_rating'+ str(batch_no)+ '.csv', index = False)
    batch_no+=1
