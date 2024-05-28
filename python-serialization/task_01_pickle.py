#!/usr/bin/env python3
"""Python Module to serialize and deserialize \
custom Python objects using the pickle module."""
import pickle

class CustomObject:
    """Custom Python object to be serialized and deserialized."""

    def __init__(self, name, age, is_student):
        """this is the constructor method for the CustomObject class."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """This method displays the attributes of the object."""
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)
    
    def serialize(self, filename):
        """This method serializes the object to a file."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None
         
    @classmethod
    def deserialize(cls, filename):
        """This method deserializes the object from a file."""
        try:        
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception:
            return None
