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
