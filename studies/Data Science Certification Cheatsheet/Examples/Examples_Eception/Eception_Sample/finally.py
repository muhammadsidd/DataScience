"""
Created on Jun 20, 2017

@author: SummitWorks
"""


def getkids():
    try:
        val = int(input("how many kids have you? "))
    except Exception:
        print("Error - ")
        return "yer wot?"
    else:
        print("are they good")
    finally:
        print("T time")
    print(val)
    return val


getkids()
getkids()
getkids()
