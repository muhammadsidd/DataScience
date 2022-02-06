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