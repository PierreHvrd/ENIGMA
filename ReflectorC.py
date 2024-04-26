# this file contains the code only for the ReflectorC
from Reflector_abstract import Reflector


class ReflectorC(Reflector):
    def __init__(self):
        self.reflection = {"A": "F", "B": "V", "C": "P", "D": "J", "E": "I", "G": "O", "H": "Y", "K": "R", "L": "Z",
                           "M": "X", "N": "W", "Q": "T", "S": "U"}
        self.type = "C"
