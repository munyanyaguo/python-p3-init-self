#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

    def breed_information(self):
        return f"{self.name} is a {self.breed}."

fido = Dog("Fido")                      # breed will be "Mutt"
spot = Dog("Spot", "Dalmatian")        # breed will be "Dalmatian"
