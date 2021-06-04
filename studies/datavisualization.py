from matplotlib import pyplot as plt
import numpy as np 
import pandas as pd
from collections import Counter

plt.style.use('fivethirtyeight')

ages_x = [25,26,27,28,29,30,31,32,33,34,35]
dev_y =[38200,45600,59033,61344,66124,71856,89167,91178,91699,93200,94000]
py_dev_y = [45372,48876,53850,63106,65889,70003,70000,71496,75370,83650,90000]

x_indexes = np.arange(len(ages_x))
width = 0.25
language_counter = Counter()
data = pd.read_csv('data.csv') ## reads into a dataFrame

for response in data['LanguagesWorkedWith']:
    language_counter.update(response.split(';')) ## returns a tuple with (language, frequency of occurance)

languages = []
popularity = []

for item in language_counter.most_common(20000):
    languages.append(item[0])
    popularity.append(item[1])

print(list(zip(languages,popularity)))

#******************LINE GRAPH ***************************************
# plt.plot(ages_x,dev_y, color ='k', linestyle = '--', marker='+', label = "All Devs")
# plt.plot(ages_x,py_dev_y,marker = 'o', linewidth = 3, label = "Python Devs") #arguments are x axis, yaxis, format (eg color followed by type of line), legend label

#####################BAR GRAPH ##############################
plt.bar(x_indexes-width,dev_y, width = width, color ='#e5ae38', label="All Devs")
plt.bar(x_indexes,py_dev_y, width = width, color ='#008fd5', label="All Devs")

plt.xticks(ticks=x_indexes, labels= ages_x) ## To replace indexes (x_indexes) with ages_x list

######################## PLOTING CODE (COMMON FOR ALL PLOTS)########################
plt.title('Median Salary in U$D by AGE')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.legend() #Passing values in a list on first plot first legend label bases
##plt.grid(True)
plt.tight_layout()

plt.savefig('plot.png')
plt.show()

