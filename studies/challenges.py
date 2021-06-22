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