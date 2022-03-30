"""
Created on Jun 20, 2017

@author: SummitWorks
"""
try:
    a = 10
    print(a)
    raise ZeroDivisionError("hello")  # 12/0 let me check python doc, its not good, only for user defind exception
except ZeroDivisionError as e:
    print("An exception occurred")
    print(e)
