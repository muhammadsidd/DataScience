import random
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
listThree = []
for e in range(0,len(listOne)):
    if e%2!=0:
        listThree.append(listOne[e])
for i in range(0, len(listTwo)):
    if i%2 == 0:
        listThree.append(listTwo[i])
print(listThree)
#####################################################################
print("")
print("Number2")
print("")
sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
l1=[]
sampleList.reverse()
l1 = sampleList[:3:]
l2 = sampleList[3:6:]
l3 = sampleList[6:9:]
print(l3)
print(l2)
print(l1)
#######################################################################
print("")
print("Number3")
print("")
list_orig=[11, 45, 8, 11, 23, 45, 23, 45, 89]
mydict={}
for e in list_orig:
    mydict[e]=list_orig.count(e)
print(mydict)
print("")
########################################################################
print("")
print("Number 4")
print("")
fl = [2, 3, 4, 5, 6, 7, 8]
sl = [4, 9, 16, 25, 36, 49, 64]
s=set()
s.update(zip(fl,sl))
print(s)

########################################################################
print("")
print("Number 5")
print("")
rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
new_list=[]
for e in sampleDict:
    if sampleDict[e] in rollNumber:
        new_list.append(sampleDict[e])

print(new_list)
########################################################################
print("")
print("number 6")
print("")
speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44,
'Sept':54}
l =[]
for e in speed:
    if speed[e] not in l:
        l.append(speed[e])
print(l)
#########################################################################
print("")
print("Number 7")
print("")
sampleList = [87, 45, 41, 65, 94, 41, 99, 94]
l1=[]
for i in range(0,len(sampleList)):
    if sampleList[i] not in l1:
        l1.append(sampleList[i])
t1=tuple(l1)
print("minimum ", min(t1))
print("maximum ",max(t1))
############################################################################
print("")
print("Number 8")
print("")
numbers = [45, 22, 14, 65, 97, 72]
for i in range(0,len(numbers)):
    if numbers[i]%3==0 and numbers[i]%5==0:
        numbers[i]="fizzbuzz"
    elif numbers[i]%3==0:
        numbers[i]="fizz"
    elif numbers[i]%5==0:
        numbers[i]="buzz"
print(numbers)
###########################################################################
print("")
print("Number 9")
print("")
animals = [ {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
{'type': 'elephant', 'name': 'Devon', 'age': 3},
{'type': 'puma', 'name': 'Moe', 'age': 5} ]
lis=[]

for e in animals:
    for i in e:
        if i == 'age':
           lis.append(e[i])
lis1= sorted(lis)
animals_sorted=[]
for i in lis1:
    for e in animals:
        for j in e:
            if i == e[j]:
                animals_sorted.append(e)
print(animals_sorted)
############################################################################
print("")
print("Number 10")
print("")
all_words = "all the words in the world".split()
def get_random_word():
    return random.choice(all_words)
s=""
i=0
x=set()
commasep=[]
unique_list=[]
while i< 1000:
    s+=get_random_word()+","
    i+=1
commasep=s.split(",")
#i have no idea why set would not remove the duplicated values.
x=(commasep)
##ABOVE SET DATASET DID NOT WORK SO I CREATED A DIFFERENT DATASTRUCTURE WITH MEMBERSHIP OPERATOR
for e in commasep:
    if e not in unique_list:
        unique_list.append(e)
print(unique_list)
########################################################################################
print("")
print("NUMBER 11")
print("")
cowboy = {'age': 32, 'horse': 'mustang', 'hat_size': 'large'}
user = input("enter attribute of cowboy u wish to get: ")
if user == 'name':
    cowboy[user] =  'The Man with No Name'
for e in cowboy:
    if e == user:
        print(cowboy.get(user))
##########################################################################################
print("")
print("NUMBER 12")
print("")
user_input = int(input("Enter a value or 0 to exit: "))
num=[]
num.append(user_input)
while user_input != 0:
    user_input = int(input("Enter a value or 0 to exit: "))
    num.append(user_input)
num.remove(min(num))
num_2=sorted(num)
for i in range(0,len(num_2)):
    print(num_2[i])
##########################################################################################
print("")
print("NUMBER 13")
print("")
number_list=[]
negative_list=[]
zero_list=[]
pos_list=[]
user_input=input("enter integers as space separated value press enter to exit ")
number_list=user_input.split()
for i in range(0,len(number_list)):
    number_list[i]=int(number_list[i])
print(number_list)
for i in range(0,len(number_list)):
    if number_list[i]< 0:
        negative_list.append(number_list[i])
    elif number_list[i]== 0:
        zero_list.append(number_list[i])
    else:
        pos_list.append(number_list[i])

l3 = negative_list+zero_list+pos_list
print(l3)
