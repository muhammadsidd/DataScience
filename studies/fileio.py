
try:
    f = open('data.txt', 'r') #r - read w- write a-append r+ read + write
    if f.name == "sometrash name":
        raise Exception

except Exception as e:
    print(e ,"Error")
else:  
    print(f.mode)
    print(f.name)
finally:
    print("done")
    f.close()

#always use context manager with file io, this will close the file 
#automatically and deal with all the exceptions 
emptylist = []
with open('data.txt', 'r') as a:
    # s = a.readline()
    # s = a.readlines()
    # s = a.read()
    for line in a:
        emptylist.append(line.split(','))
    print (emptylist)

for z in range(0,len(emptylist)):
    if z % 2 != 0:
        print(list(zip(emptylist[z-1],emptylist[z])))

with open('data.txt', 'r') as b:
    b_contents = b.read(20)
    print('cursor after 20 characters here')
    print(b_contents)
    b_contents = b.read(20)
    print('cursor after 40 characters here')
    print(b_contents)

    
