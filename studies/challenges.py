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