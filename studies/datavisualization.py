from re import T
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter

plt.style.use('fivethirtyeight')

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38200, 45600, 55033, 67344, 69124,
         71856, 72167, 73178, 73699, 79200, 84000]
py_dev_y = [45372, 48876, 53850, 63106, 65889,
            70003, 70000, 71496, 75370, 73650, 90000]

x_indexes = np.arange(len(ages_x))
width = 0.25
language_counter = Counter()
data = pd.read_csv('data.csv')  # reads into a dataFrame

############# CLEANING DATA #########################
#data = data.dropna(axis='index', how='any')
    #any = drop the record index(row) if any value is missing
    #all = delete the record if and only if all values are missing 
    #axis = 'index' for rows 'coloumns' for columns
for response in data['LanguagesWorkedWith']:
    # returns a tuple with (language, frequency of occurance)
    language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(6):
    languages.append(item[0])
    popularity.append(item[1])

print(list(zip(languages, popularity)))

dframe = pd.DataFrame({"Age":ages_x,"Python_Dev": py_dev_y, "All_Devs" : dev_y})
dframe.set_index("Age", inplace=True)
# dframe["Difference"] = dframe["Python_Dev"].apply(lambda x: x - dframe["All_Devs"])
dframe["Difference"] = dframe["Python_Dev"] - dframe["All_Devs"]

print(dframe)
# ******************LINE GRAPH ***************************************
plt.plot(ages_x,dev_y, color ='k', linestyle = '--', marker='+', label = "All Devs")
plt.plot(ages_x,py_dev_y,marker = 'o', linewidth = 3, label = "Python Devs") #arguments are x axis, yaxis, format (eg color followed by type of line), legend label
plt.title('Median Salary in U$D by AGE')
plt.xlabel('Age')
plt.ylabel('Salary')
# med = np.median(py_dev_y)
plt.fill_between(ages_x, py_dev_y, dev_y, where=py_dev_y <= dev_y, interpolate= True, color='red', alpha =0.25)
plt.fill_between(ages_x, py_dev_y, dev_y, where=py_dev_y >= dev_y, interpolate= True,color = 'k', alpha =0.25)
plt.legend() #Passing values in a list on first plot first legend label bases
plt.grid(True)
plt.tight_layout()
plt.savefig('line.png')
plt.show()
#####################BAR GRAPH ##############################
plt.bar(x_indexes-width,dev_y, width = width, color ='#e5ae38', label="All Devs")
plt.bar(x_indexes,py_dev_y, width = width, color ='#008fd5', label="All Devs")
plt.xticks(ticks=x_indexes, labels= ages_x) ## To replace indexes (x_indexes) with ages_x list
plt.title('Median Salary in U$D by AGE')
plt.xlabel('Age')
plt.ylabel('Salary')

plt.legend() #Passing values in a list on first plot first legend label bases
plt.grid(True)
plt.tight_layout()

plt.savefig('Bar.png')
plt.show()

########################## Languages and popularity Horizontal Bar ##############
colors = ['blue', 'green', 'yellow', 'black', 'brown', 'orange']
plt.barh(languages,popularity)
plt.title("popular languages")
plt.ylabel("programming languages")
plt.xlabel(" number of programers")

plt.tight_layout()
plt.show()
plt.savefig('Barh.png')

############################# Languages and popularity Pie chart ########################
exp = []
value = 0

for language in languages:

    if language == 'Python':
        value = 0.1
    else:
        value = 0

    exp.append(value)

# can also add colors = colors in the argument for plt.pie()
plt.pie(popularity, labels=languages, explode=exp, shadow=True,
        wedgeprops={'edgecolor': 'white'}, startangle=45, autopct='%1.1f%%',
        )

plt.tight_layout()
plt.show()
plt.savefig('Pie.png')

############################################# Stack Plots ##################################
minutes = ['1','2','3','4','5','6','7','8','9','10']
player1 = [8, 6, 5, 4, 3, 2, 1, 1, 1,0]
player2 = [0, 1, 2, 3, 3, 3, 3, 4, 3,2]
player3 = [0, 1, 1, 1, 2, 3, 4, 3, 4,6]

labels = ['player1', 'player2', 'player3']
colors = ['#6d904f', '#fc4f30', '#008fd5']

plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)

plt.legend(loc=(0.07, 0.05)) ##tuple is a cordinate (x,y)

plt.title("My Awesome Stack Plot")
plt.tight_layout()
plt.show()
plt.savefig("stackplt.png")

################################# sin cosine #########################################
x_f =np.array([0,45,90,135,180,225,270,315,360])
f_s=[]

for x in x_f:
    f = np.sin(x)
    f_s.append(f)

plt.plot(x_f,f_s)
plt.xlabel("Angle in Degrees")
# plt.xticks(f_s)
plt.ylabel("f(Sin(x))")
plt.tight_layout()
plt.show()

################################ Histograms ###########################################

ages = [18,19,20,18,20,18,19,23,22,23,23,23,25,26,27,28,28,29,30,31,32,35,35,45,55]
bins = [10,20,30,40,50,60]
med = np.median(ages)
plt.hist(ages, bins=bins, edgecolor = 'black' ) #can add log = True in parameters to display y vlaues as power of 10
plt.axvline(med, label = "median line", color = 'red', linewidth = 2)
plt.legend()
plt.show()

########################### SCATTER PLOT #############################################

x= [1,2,3,4,5,6,7,8,9,10]
y= [7,4,5,3,6,8,9,0,1,2]

plt.scatter(x,y,s=100, c= 'green', marker='x', edgecolors='black',linewidths=1, alpha=0.75)
plt.xlabel("seconds")
plt.ylabel("hits")
plt.grid(True)
plt.tight_layout()
plt.show()