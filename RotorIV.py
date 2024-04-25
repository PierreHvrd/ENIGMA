# this file contains the code only for the rotor IV
from Rotor_abstract import Rotor


class RotorIV(Rotor):
    def __init__(self, initial_position):
        Rotor.__init__(self, initial_position)
        self.ring = {"A": "E", "B": "S", "C": "O", "D": "V", "E": "P", "F": "Z", "G": "J", "H": "A", "I": "Y", "J": "Q",
                     "K": "U", "L": "I", "M": "R", "N": "H", "O": "X", "P": "L", "Q": "N", "R": "F", "S": "T", "T": "G",
                     "U": "K", "V": "D", "W": "C", "X": "M", "Y": "W", "Z": "B"}

        self.notch = "K"
        self.double_stepping = "J"
        self.type = "IV"
