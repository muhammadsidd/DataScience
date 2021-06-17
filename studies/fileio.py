
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
    print(b.tell()) # tells which character we are on in the file at current time
    b.seek(0) #set file cursor to 0th character and start over you may change seek position to anywhere u like

with open('data2.txt', 'w') as f:
    f.write('test')

# how to copy pictures using binary read and write 
# with open('some.jpg','rb') as rf:
#     with open('some_copy.jpg','wb') as wf:
#         for line in rf:
#             wf.write(line)


    
