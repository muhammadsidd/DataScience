'''
Created on Jun 21, 2017

@author: SummitWorks
'''
import time
import datetime
 
print("Time in seconds since the epoch: %s" %time.time())
print("Current date and time: " , datetime.datetime.now())
print("Or like this: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))
 
 
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day4_list_tuple_dictionary of year: ", datetime.date.today().strftime("%j"))
print("Day4_list_tuple_dictionary of the month : ", datetime.date.today().strftime("%d"))
print("Day4_list_tuple_dictionary of week: ", datetime.date.today().strftime("%A"))
print(datetime.datetime.tzinfo)