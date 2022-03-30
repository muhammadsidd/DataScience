'''
Created on May 12, 2016

@author: Administrator
'''
#Python program that creates new, empty file

# Create new empty file.
# ... If the file exists, it will be cleared of content.
# f = open("E:\\test.txt", "w")

with open("E:\\test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")
f.close()



f = open("E:\\test.txt", "r")
print(f.read(15))
# read line by line, len function to get lenth of the line. do this till end of the file
# count = 0
# for line in f:
#     count += len(line)
#     print(line)
# print("Total Character Count = " , count)
# f.close()
