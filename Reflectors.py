# this file contains all the classes for the reflectors
from abc import ABC, abstractmethod


class Reflector(ABC):
    @abstractmethod
    def __init__(self):
        self.reflection = {}
        self.type = ""

    def cypher(self, letter):
        for key, value in self.reflection.items():
            if letter == key:
                return value

            elif letter == value:
                return key

    def print_type(self):
        print(f"The reflector is type: {self.type}")


class ReflectorB(Reflector):
    def __init__(self):
        self.reflection = {"A": "Y", "B": "R", "C": "U", "D": "H", "E": "Q", "F": "S", "G": "L", "I": "P", "J": "X",
                           "K": "N", "M": "O", "T": "Z", "V": "W"}

        self.type = "B"


class ReflectorC(Reflector):
    def __init__(self):
        self.reflection = {"A": "F", "B": "V", "C": "P", "D": "J", "E": "I", "G": "O", "H": "Y", "K": "R", "L": "Z",
                           "M": "X", "N": "W", "Q": "T", "S": "U"}
        self.type = "C"
