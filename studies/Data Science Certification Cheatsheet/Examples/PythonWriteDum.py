'''
Created on May 12, 2016

@author: Administrator
'''
#Dump: This writes the list contents in binary form to the file f.pickle. 
#The extension (pickle) has no importance.
#Python program that uses pickle, list

import pickle

# Input list data.
list = ["one", "two", "three"]
print("before:", list)

# Open the file and call pickle.dump.
with open("f.pickle", "wb") as f:
    pickle.dump(list, f)

# Open the file and call pickle.load.
with open("f.pickle", "rb") as f:
    data = pickle.load(f)
    print("after:", data)