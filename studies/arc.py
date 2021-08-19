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