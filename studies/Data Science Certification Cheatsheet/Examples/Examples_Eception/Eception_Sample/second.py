'''
Created on Jun 20, 2017

@author: SummitWorks
'''
while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        # break
    except ValueError:
        print("No valid integer! Please try again ...")
    else:
        print("hello, i am from else block")
        break
print("Great, you successfully entered an integer!")