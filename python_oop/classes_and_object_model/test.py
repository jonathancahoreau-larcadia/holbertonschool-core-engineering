#!/usr/bin/env python3
"""
test.py
Test de la classe Square du module 6-square.
"""

Square = __import__('6-square').Square

my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)
class Animal:
    def speak(self):
        print("sound animal!")

class Dog(Animal):
    def aboi(self):
        print("wouaf!")

class Cat(Animal):
    def miaul(self):
        print("miaou")

dog = Dog()
dog.aboi()

cat = Cat()
cat.miaul()

animals = [Cat(), Dog()]

for animal in animals:
    animal.speak()
