# this file contains the code only for the rotor I
from .Rotor_abstract import Rotor


class RotorI(Rotor):
    def __init__(self, initial_position):
        Rotor.__init__(self, initial_position)
        self.ring = {"A": "E", "B": "K", "C": "M", "D": "F", "E": "L", "F": "G", "G": "D", "H": "Q", "I": "V", "J": "Z",
                     "K": "N", "L": "T", "M": "O", "N": "W", "O": "Y", "P": "H", "Q": "X", "R": "U",
                     "S": "S", "T": "P", "U": "A", "V": "I", "W": "B", "X": "R", "Y": "C", "Z": "J"}

        self.notch = "R"
        self.double_stepping = "Q"
        self.type = "I"
