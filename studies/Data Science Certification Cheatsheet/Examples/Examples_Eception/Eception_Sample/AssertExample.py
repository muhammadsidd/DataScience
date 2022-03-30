"""
Created on Jun 20, 2017

@author: SummitWorks
"""


def KelvinToFahrenheit(Temperature):
    try:
        assert (Temperature >= 0), "Colder than absolute zero!"  # testing, in unit testing.
    except AssertionError as e:
        print(e)
        print("you have given negative temp")
    else:
        return ((Temperature - 273) * 1.8) + 32


# print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.78)))
# print(KelvinToFahrenheit(-5))
