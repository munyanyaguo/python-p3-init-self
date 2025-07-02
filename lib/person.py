#!/usr/bin/env python3

class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, my name is {self.name}."
    
guido = Person("Guido")  # Example instantiation
