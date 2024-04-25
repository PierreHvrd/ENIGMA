# this file contains the code only for the rotor III
from Rotor_abstract import Rotor


class RotorIII(Rotor):
    def __init__(self, initial_position):
        Rotor.__init__(self, initial_position)
        self.ring = {"A": "B", "B": "D", "C": "F", "D": "H", "E": "J", "F": "L", "G": "C", "H": "P", "I": "R", "J": "T",
                     "K": "X", "L": "V", "M": "Z", "N": "N", "O": "Y", "P": "E", "Q": "I", "R": "W",
                     "S": "G", "T": "A", "U": "K", "V": "M", "W": "U", "X": "S", "Y": "Q", "Z": "O"}

        self.notch = "W"
        self.double_stepping = "V"
        self.type = "III"
