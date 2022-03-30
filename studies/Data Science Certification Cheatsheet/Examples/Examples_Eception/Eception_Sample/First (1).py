'''
Created on Jun 20, 2017

@author: SummitWorks
'''


# print("opening data base connection")
# print("i modified some data in the table")
# n1 = int(input("Please enter a number: "))
# n2 = int(input("Please enter a number: "))
# print(n1/n2) # app terminates abnormally.raise exception,
# print("Please enter integer value only")
# print("Please enter proper values, we cant divide with zero")
#
# print("there is a problem with  your data, please try again with valid data...")
# print("close the connection") # imp statments for app for security
# print("close the session")
# print("clear cache")
#
# print(chr(97))

#
# print("opening data base connection")
# print("i modified some data in the table")
# try:
#     n1 = int(input("Please enter a number: "))
#     n2 = int(input("Please enter a number: "))
#     print(n1/n2) # app terminates abnormally.raise exception,
# except ValueError:
#     print("Please enter integer value only")
# except ZeroDivisionError:
#     print("Please enter proper values, we cant divide with zero")
#
# print("there is a problem with  your data, please try again with valid data...")
# print("close the connection") # imp statments for app for security
# print("close the session")
# print("clear cache")
#
# print(chr(97))
#
while True:
    try:
        # sending the money , send money with invalid account country to contry
        # dont add entire script here.
        n1 = int(input("Please enter a number: ")) # python interpreter will identified Exception, raise the exccep
        n2 = int(input("Please enter a number: "))
        print(n1/n2)  # application terminates abnomally, python will raise automatically.
        # i like to execute some imp statements
        # can i add imprtant statemens here..
    except ValueError as v: # specific way, good way
        # cancel the transction
        # send a email to sedner, intiate refund process.
        # send SMS
        print(" got a unexpected issue since you entered invalid data")
        print(v)
        continue
        # can i add imprtant statemens here..
        # are you executing all the time

    except ZeroDivisionError:
        print("you are dividing with zero, which is not possible")
        continue
    except: # its generic, it will handle all exception
        print("hello some other exception raised")
    else:
        print("at the end, in else block")
        # conformation email to sender
        # can i add imprtant statemens here..
        break
    # i cant keep those imp statemets in else block

    finally:   # if you have exeption , dont have any exception we will execute finaly block without fail
        # mandatory statements, clear cache, close the resources, delete cookie, disable session.
        print("at end of the application, in finally block")
        print(" i have save the data") # all mandatory statements of the application
        print("close the connection")