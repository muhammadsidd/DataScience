from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter

plt.style.use('fivethirtyeight')

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38200, 45600, 59033, 61344, 66124,
         71856, 89167, 91178, 91699, 93200, 94000]
py_dev_y = [45372, 48876, 53850, 63106, 65889,
            70003, 70000, 71496, 75370, 83650, 90000]

x_indexes = np.arange(len(ages_x))
width = 0.25
language_counter = Counter()
data = pd.read_csv('data.csv')  # reads into a dataFrame

for response in data['LanguagesWorkedWith']:
    # returns a tuple with (language, frequency of occurance)
    language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(6):
    languages.append(item[0])
    popularity.append(item[1])

print(list(zip(languages, popularity)))


# ******************LINE GRAPH ***************************************
plt.plot(ages_x,dev_y, color ='k', linestyle = '--', marker='+', label = "All Devs")
plt.plot(ages_x,py_dev_y,marker = 'o', linewidth = 3, label = "Python Devs") #arguments are x axis, yaxis, format (eg color followed by type of line), legend label
plt.title('Median Salary in U$D by AGE')
plt.xlabel('Age')
plt.ylabel('Salary')
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
plt.xticks(f_s)
plt.ylabel("f(Sin(x))")
plt.tight_layout()
plt.show()