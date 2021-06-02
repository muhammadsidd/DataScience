from numpy import index_exp
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
print(df.head(3)) ##only 3 rows
print(df.tail(2)) #last 2
## mer = pd.merge(df,record1, on="Day") //will merge on the key. SHOULD HAVE SAME KEY for on = 

joined = df.join(record1) #join the two using the same index. 
print(joined)

 ##### Make key your index ########
df.set_index("Downloads", inplace=True)
df.plot()
plt.pyplot.show()

##Change colomn headers ##
df = df.rename(columns={"watched":"Users"})
print(df)

concate = pd.concat([df,record1]) #going to default to num index if same index for first dataset and second dataset
print(concate)
