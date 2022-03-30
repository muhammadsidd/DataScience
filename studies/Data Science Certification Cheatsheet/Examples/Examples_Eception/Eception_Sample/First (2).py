
try:
    # sending the money , send money with invalid account country to country, placing an order
    # Open a DB connection, file to read/write
    # don't add entire script here.
    n1 = int(input("Please enter a number: "))
    n2 = int(input("Please enter a number: "))
    print(n1/n2) # app terminates abnormally.raise exception,
    # To execute some imp statements like closing DB conn, use other blocks

except ValueError as v: # specific way, good way
    # cancel the transaction, send a email to sender, initiate refund process.
    print("Got an unexpected issue since you entered invalid data. \nPlease enter integer value only")

except ZeroDivisionError:
    print("Please enter proper values, we cant divide with zero")

except: # its generic, it will handle all exception
    print("hello some other exception raised")

else:
    # conformation email to sender
    print("In else block")
finally:
    # Irrespective of an exception raised or not, finally block will execute without fail
    #  all mandatory statements of the application, clear cache, close the resources, delete cookie, disable session.
    print("In finally block")

print("at end of the application")

  
