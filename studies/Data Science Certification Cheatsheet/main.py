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