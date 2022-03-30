try:
    fh = open("testfile", "r+")
    print(fh.readline())
    fh.write("\nThis is statement is written from try block")
except IOError:
    print("Error: can\'t find file or read data")
    # we can convert , handle the exception
    # we can rollback(), update 
else:
    print("Read content in the file successfully")
    fh.close()
print("hello, i am last line of the program")