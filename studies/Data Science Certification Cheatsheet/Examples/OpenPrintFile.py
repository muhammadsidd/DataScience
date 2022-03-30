'''
Created on May 12, 2016

@author: Administrator
'''
#Python program that reads all lines

# Open a file on the disk.
f = open(r"E:\python.txt", "r")
f.readline()
# Print all its lines.
for line in f.readlines():
    print(line)
