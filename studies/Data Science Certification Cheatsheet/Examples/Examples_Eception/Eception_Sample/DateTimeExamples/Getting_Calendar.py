'''
Created on Jun 21, 2017

@author: SummitWorks
'''
import calendar

cal = calendar.month(2018,6)
print("Here is the calendar:")
print(cal)
print(calendar.TextCalendar(calendar.SUNDAY).formatyear(2017, 2, 1, 1, 3))