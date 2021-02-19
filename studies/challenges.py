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


k = mid("aaaa")
print(k)