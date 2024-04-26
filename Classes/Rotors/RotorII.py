# this file contains the code only for the rotor II
from .Rotor_abstract import Rotor


class RotorII(Rotor):
    def __init__(self, initial_position):
        Rotor.__init__(self, initial_position)
        self.ring = {"A": "A", "B": "J", "C": "D", "D": "K", "E": "S", "F": "I", "G": "R", "H": "U", "I": "X", "J": "B",
                     "K": "L", "L": "H", "M": "W", "N": "T", "O": "M", "P": "C", "Q": "Q", "R": "G",
                     "S": "Z", "T": "N", "U": "P", "V": "Y", "W": "F", "X": "V", "Y": "O", "Z": "E"}

        self.notch = "F"
        self.double_stepping = "E"
        self.type = "II"
