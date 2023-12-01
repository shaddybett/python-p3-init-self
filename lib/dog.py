#!/usr/bin/env python3

class Dog:
    def __init__(self,name,breed='Mutt'):
        self.name = name
        self.breed = breed
    def __str__(self) -> str:
        return f'{self.name} {self.breed}'
         


d = Dog('fido','chiuawawa')
print(d)