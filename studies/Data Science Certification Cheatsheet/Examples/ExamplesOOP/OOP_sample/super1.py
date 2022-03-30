'''
Created on Nov 2, 2018

@author: SummitWorks
'''


class Animal:
    def __init__(self, animalName):
        print(animalName, 'is an animal.');


class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
        super().__init__(mammalName)


class NonWingedMammal(Mammal):
    def __init__(self, NonWingedMammalName):
        print(NonWingedMammalName, "can't fly.")
        super().__init__(NonWingedMammalName)


class NonMarineMammal(Mammal):
    def __init__(self, NonMarineMammalName):
        print(NonMarineMammalName, "can't swim.")
        super().__init__(NonMarineMammalName)


# class Dog(NonMarineMammal, NonWingedMammal):
#     def __init__(self):
#         print('Dog has 4 legs.');
#         super().__init__('Dog')
#

bat = NonMarineMammal('Bat')

# d = Dog()
# print('')

