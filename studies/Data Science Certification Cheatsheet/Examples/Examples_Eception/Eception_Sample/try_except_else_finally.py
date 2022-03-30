"""
Created on Jul 27, 2017
@author: SummitWorks
"""


# for i in range(10):
#     if i==5:
#         continue
#     print(i)

def askint():
    while True:
        try:
            val = int(input("Please enter an integer: "))
        except:
            print("Looks like you did not enter an integer!")
            continue
        else:
            print('Yep thats an integer!')
            break
        finally:
            print("Finally, I executed!")
        print(val)


askint()
