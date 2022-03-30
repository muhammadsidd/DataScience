'''
Created on Jun 21, 2017

@author: SummitWorks
'''
import time;  # This is required to include time module.

ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)
import calendar

cal = calendar.month(2017,12)
print(cal)

import datetime
t = datetime.time(4,20,1)
print(t.tzinfo)
print(t.hour)