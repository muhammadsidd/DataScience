from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

ages_x = [25,26,27,28,29,30,31,32,33,34,35]
dev_y =[38200,45600,59033,61344,66124,71856,89167,91178,91699,93200,94000]
py_dev_y = [45372,48876,53850,63106,65889,70003,70000,71496,75370,83650,90000]
plt.plot(ages_x,dev_y, color ='k', linestyle = '--', marker='+', label = "All Devs")
plt.plot(ages_x,py_dev_y,marker = 'o', linewidth = 3, label = "Python Devs") #arguments are x axis, yaxis, format (eg color followed by type of line), legend label
plt.title('Median Salary in U$D by AGE')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.legend() #Passing values in a list on first plot first legend label bases
##plt.grid(True)
plt.tight_layout()

plt.savefig('plot.png')
plt.show()

