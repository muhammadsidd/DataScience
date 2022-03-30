'''
Created on May 12, 2016

@author: Administrator
'''
#Python program that counts characters in file

# Open a file.
f = open(r"E:\test.txt", "r")

# Stores character counts.
chars = {}

# read line by line, len function to get lenth of the line. do this till end of the file
count = 0
for line in f:
    count += len(line)
    #print(line)
print("Line Count = " , count)

# Loop over file and increment a key for each char.
for line in f.readlines():
    for c in line.strip():
        #The method strip() returns a copy of the string in which all chars have been stripped
        #from the beginning and the end of the string (default whitespace characters).

        # Get existing value for this char or a default of zero.
        # ... Add one and store that.
        chars[c] = chars.get(c, 0) + 1

# Print character counts.
for item in chars.items():
    print("item = " , item)