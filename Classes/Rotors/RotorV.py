# this file contains the code only for the rotor V
from .Rotor_abstract import Rotor


class RotorV(Rotor):
    def __init__(self, initial_position):
        Rotor.__init__(self, initial_position)
        self.ring = {"A": "V", "B": "Z", "C": "B", "D": "R", "E": "G", "F": "I", "G": "T", "H": "Y", "I": "U", "J": "P",
                     "K": "S", "L": "D", "M": "N", "N": "H", "O": "L", "P": "X", "Q": "A", "R": "W", "S": "M", "T": "J",
                     "U": "Q", "V": "O", "W": "F", "X": "E", "Y": "C", "Z": "K"}

        self.notch = "A"
        self.double_stepping = "Z"
        self.type = "V"
