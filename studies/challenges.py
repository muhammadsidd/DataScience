import math

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

# def online_count(dick):
#     count = 0
#     for k,v in dick.items():
#         if v == "online":
#             count +=1
#     return count
# statuses = {
#     "Alice": "online",
#     "Bob": "offline",
#     "Eve": "online",
# }