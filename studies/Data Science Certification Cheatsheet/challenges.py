import math
######################## Challenge 1########################
def capital_indexes(cap):
    l1=[]
    for i in range(0,len(cap)):
        print(cap[i])
        if cap[i].isupper() == True:
            print('here')
            l1.append(i)
        else:
            continue
    print(l1)
    return l1
######################## challenge 2###################################
def mid(str):
    if (len(str) % 2 == 0):
        return ""
    else:
        k = math.ceil(len(str) / 2)
        return str[k - 1]

def mid1(string):
    if len(string) % 2 == 0:
        return ""
    return string[len(string)//2]

k = mid1("acb")
print(k)
########################## challenge 3##################################
def online_count(dick):
    count = 0
    for k,v in dick.items():
        if v == "online":
            count +=1
    return count
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

from random import randint

###################################challenge 4################################
def random_number():
    return randint(1, 101)


print(random_number())


################### Challenge 5#################################################
#isinstance(a,int) == true will not work becuz isinstace(True, int) will return True
def only_ints(a, b):
    if type(a) == int and type(b) == int:
        return True
    else:
        return False


print(only_ints(1, 'a'))
###################### Final Challenge #####################################
def format_number(num):
    if num > 0:
        vach1 = str(num)[::-1]
    count = 0
    l1=[]
    for i in range (0, len(vach1)):
        count +=1
        l1.append(vach1[i])
        if count == 3 and i != len(vach1)-1:
            l1.append(',')
            count = 0
    e = "".join(l1)
    return e[::-1]

this = format_number(100000000)
print (this)

################### Sorting Dictionary ######################

d = {"Oranges":5, "Apple":19, "James":10}

sd = { k : v for k,v in sorted(d.items(), key = lambda v: v[1])} ##sorted by value
sd = { k : v for k,v in sorted(d.items(), key= lambda v: v[0])} ## sorted by key
print(sd)

################## MAP and Filter ########################

# l1 = ['argentina','pakistan','india','USA']
# l2 = [12,24,23,14]

# l1_l2 = map((lambda k,v: k[0], v[0]),(l1,l2))
# print(list(l1_l2))

def somefunction(keyFunction, values):
    return dict((keyFunction(v),v) for v in values)

print(somefunction(lambda a: a[0], ["Hello","World"]))

################## delete from ditionary ##################

del d["Oranges"]
print(d)

############## custom iterator ###################

class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value +=1
        return current

nums = MyRange(1,10)

for num in nums:
    print(num)

################### Custom Generators ####################

def my_range (start):
    current = start
    while True:
        yield current
        current += 1
nums = my_range(1)

for num in nums:
    print(num)

def solution(N):
    # write your code in Python 3.6
    if (N < 10):
        return 0
    i = 0

    while N >= 10:
        N = N // 10
        i += 1
    temp = 1

    for j in range(0, i):
        temp *= 10

    return temp

## palandrome that takes care of one offset 

def pal(str, str2):
    temp = str[::-1]
    count = 0 

    for i in range(len(str2)):
        if temp[0] != str2[0]:
            count +=1
        
    if temp == str2 or count <= 1:
        return True 
    else:
        return False

print(pal('stats', 'foo'))

#### MAp type counter ######
map_data = [['A','A','A','A','U','U','U','U'],
['A','A','A','A','U','R','R','R'],
['W','W','W','W','T','T','T','T'],
['W','W','W','W','T','R','R','R'],
['C','C','U','U','T','R','U','U'],
['T','T','T','T','T','T','U','U'],
['U','U','U','U','T','R','U','U']]

def count_type(map_data,map_type):
    count = 0 
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            if map_data[i][j] == map_type:
                count +=1
    return count

res = count_type(map_data,'A')

print(res)

def classify_map(map_data):
    rows=len(map_data)
    cols=len(map_data[0])
    if (count_type(map_data,'R')/(rows*cols))>=0.5:
        print('Suburban')
    elif (count_type(map_data,'A')/(rows*cols))>=0.5:
        print('Farmland')
    elif ((count_type(map_data,'U')+count_type(map_data,'W'))/(rows*cols))>=0.5:
        print('Conservation')
    elif ((((count_type(map_data,'C')/(rows*cols))>=0.5 and ((count_type(map_data,'U')+count_type(map_data,'W'))/(rows*cols))>=0.10) or ((count_type(map_data,'U')+count_type(map_data,'W'))/(rows*cols) <=0.2))):
        print('City')
    else:
        print('Mixed')

classify_map('U')

from random import randint
#1
'''DONE'''

#2 Ceil and floor manual functions
print("########################################---NUMBER2----########################################")
print("")
a = eval(input("enter a number "))
print('ceiling value of entered number ',-(-a//1))
print('Floor value of a given number ', (a//1))


# 3 Swaping two integers using a single line
print("")
print("########################################---NUMBER3----########################################")
print("")
x = int(input("enter value of x "))
y = int(input("enter value of y "))
x,y = y,x

print('value of x ', x)
print('value of y', y)

# 4 names ternary operations
print("")
print("########################################---NUMBER4----########################################")
print("")
name = input("enter a name over here ")
print("i feel you are destineed to do wonderful things in AWS") \
    if name.lower() == "john cleese" or name.lower() == "michael palin" else print("you have a nice name ")

# 5 60% sale
print("")
print("########################################---NUMBER5----########################################")
print("")
discount=0.6
prices=[4.95, 9.95, 14.95, 19.95, 24.95]
print("PRICE\tDISCOUNT\tFINAL")
for price in prices:
    dis= price*discount
    final=price-dis
    format_dis="{:.2f}".format(dis)
    format_final="{:.2f}".format(final)
    print(str(price)+"\t"+format_dis+"\t \t"+format_final)

#6 power of the dollar
print("")
print("########################################---NUMBER6----########################################")
print("")
#fuction to calculate the power
def power(base,pwr):
    res=1
    for i in range(1,pwr+1):
        res=res*base
    return res

for i in range(1,5+1):
    print(str(i),str(i+1),str(power(i,i+1)))

#7 FLORIDA LOTTO
print("")
print("########################################---NUMBER7----########################################")
print("")
#generate a 3 digit random lotto number
winning_num= randint(100,999)
print("{}{}".format(("winning number is "),winning_num))
user  = input("enter a 3 digit number ")
count =0 #flag variable to keep track of the if statement to run
if user == str(winning_num):
    #set flag to -1 to differ from other winning conditions
    count = -1
else:
    for n in range(0,len(user)):
        if user[n] in str(winning_num):
            count+=1
        else:
            continue
#results respective of the matching numbers
if count == 1:
    print("winnings = $1000")
elif count ==2:
    print("winnings = $2000")
elif count == 3:
    print("winnings = $3000")
elif count ==-1:
    print("YOU WON $10000")
else:
    print("sorry you lost")

#8 Number the max number occurs in a given group of integers
print("")
print("########################################---NUMBER8----########################################")
print("")
#ask values from the user until 0 is entered
value = int(input("enter a value, enter 0 to exit."))
values = []
#append the values to the given empty array.
values.append(value)
#whie loops exits once 0 is entered
while value!=0:
    value = int(input("enter a value, enter 0 to exit."))
    #append all given values to the empty array as separate integers
    values.append(value)
for i in range(0,len(values)):
    print(values[i],end="")
#set max to the first element of the array is a good practice
max = values[0]
#traverse the array to find the max and swap if needed
for j in range(0,len(values)):
    if max < values[j]:
        max = values[j]
print("")
print(max)
#display count
print(values.count(max))

#9 triangular pattern
print("")
print("########################################---NUMBER9----########################################")
print("")
rows = int(input("enter number of rows: "))
var = rows
#row by row calculations
for row in range(0,rows):
    #inner loop1 keeps track of the spaces to skip
    for v in range(0,var):
        print(end=" ")
    var = var-1
    #inner loop2 prints the *
    for v in range(0,row +1):
        print(end="* ")
    print("")
    print("")

#10 number pattern
print("")
print("########################################---NUMBER10----########################################")
print("")
num = [1,2,3,4,5,6,7]
i = 0
for row in range(0,len(num)):
    for n in range(0,len(num)):
        print(str(num[n]),end=" ")
    print("")
    num[i]=''
    i = i+1

for row in range(len(num)-1,-1,-1):
    if num[row] == '':
        num[row]=row+1
        print(str(num[row]),end=" ")


# 11 the phonebook
print("")
print("########################################---NUMBER11----########################################")
print("")
#dictionary to map a value to a specific phone number
# since there are 9 different possibilities
phone = {2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],
         7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}

phone_number = input("enter the number as '-' separated value ")
#split the number with - as a delimiter to separate the extension value
extension = phone_number.split('-')[2]
print(extension)
#empty string declared to keep track of the found extension
concatstr=""
#for loop to traverse the dictionary and replace the number with the mapped key.
for ch in extension:
    for key in phone.keys():
        if ch.lower() in phone[key]:
            concatstr+=str(key)

print(phone_number.split('-')[0]+"-"+phone_number.split('-')[1]+"-"+concatstr)