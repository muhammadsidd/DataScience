import numpy as np
import pandas as pd
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
print(len(df.index))
print(df) ##only 3 rows
print(df.tail(2)) #last 2
## mer = pd.merge(df,record1, on="Day") //will merge on the key. SHOULD HAVE SAME KEY for on = 

joined = df.join(record1) #join the two using the same index. 
print(joined)

 ##### Make one key your index / primary key ########
df.set_index("Downloads", inplace=True) #inplace = True will permanently change ur dataframe 
df.plot()
plt.pyplot.show()

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

################### Groub by ########################














