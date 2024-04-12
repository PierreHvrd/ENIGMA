# file where all the rotors are defined
from abc import ABC, abstractmethod


class Rotor(ABC):
    """
    Careful with the following difference
    Type of the rotor: I-II-III-IV-V
    Physical emplacement of the rotor in the machine: 1-2-3
    """
    @abstractmethod
    def __init__(self, initial_position):
        self.position = initial_position  # capital letter
        self.ring = {}  # dictionary is close to the way a rotor was build in the actual ENIGMA machine
        self.notch = ""  # when this letter is reached the next rotor has to rotate
        self.double_stepping = ""  # when this position is reached BY THE MIDDLE ROTOR it rotates again and make the
        # next rotate this position is always the position before the notch position.

    def rotate(self):
        """
        This method rotates the rotor meaning this changes the position of the rotor.
        """
        self.position = chr(ord(self.position) + 1)
        if ord(self.position) > 90:
            self.position = "A"

    def cypher(self, letter):
        """
        Everything is this function is done with number (ascii codes of the letters) because it is
        simpler for the calculations
        :param letter: a 1 letter string
        :return encryption: a 1 letter string that is the encryption of the given letter.
        """

        # first we apply the position of the rotor
        encryption = self.cesar_cypher(letter, True)

        for key in self.ring.keys():
            if key == chr(encryption):
                encryption = ord(self.ring[key])
                break

        # finally we apply the position of the rotor to the output
        encryption = self.cesar_cypher(chr(encryption), False)

        return chr(encryption)

    def cypher_back(self, letter):
        """
        Everything is this function is done with number (ascii codes of the letters) because it is
        simpler for the calculations.
        This is the reciprocal function of cypher
        :param letter: a 1 letter string
        :return encryption: a 1 letter string that is the encryption of the given letter.
        """

        # first we apply the position of the rotor
        encryption = self.cesar_cypher(letter, True)

        for key, value in self.ring.items():
            if value == chr(encryption):
                encryption = ord(key)
                break

        # finally we apply the position of the rotor to the output
        encryption = self.cesar_cypher(chr(encryption), False)

        return chr(encryption)

    def cesar_cypher(self, letter, plus):
        """
        Simple cesar cypher but the key is self.position. Useful to apply the position of the rotor
        :param letter: a 1 letter string
        :param plus: a boolean that tells if the cypher is positive (A -> B, B-> C) or negative (B-> A, C-> B)
        :return: cypher: a number that represents the letter cyphered
        """
        if plus:
            cypher = (ord(letter) - 65 + ord(self.position) - 65) % 26
            return cypher + 65
        else:
            cypher = (ord(letter) - 65 - (ord(self.position) - 65)) % 26
            return cypher + 65


class RotorI(Rotor):
    def __init__(self, initial_position):
        Rotor.__init__(self, initial_position)
        self.ring = {"A": "E", "B": "K", "C": "M", "D": "F", "E": "L", "F": "G", "G": "D", "H": "Q", "I": "V", "J": "Z",
                     "K": "N", "L": "T", "M": "O", "N": "W", "O": "Y", "P": "H", "Q": "X", "R": "U",
                     "S": "S", "T": "P", "U": "A", "V": "I", "W": "B", "X": "R", "Y": "C", "Z": "J"}

        self.notch = "R"
        self.double_stepping = "Q"


class RotorII(Rotor):
    def __init__(self, initial_position):
        Rotor.__init__(self, initial_position)
        self.ring = {"A": "A", "B": "J", "C": "D", "D": "K", "E": "S", "F": "I", "G": "R", "H": "U", "I": "X", "J": "B",
                     "K": "L", "L": "H", "M": "W", "N": "T", "O": "M", "P": "C", "Q": "Q", "R": "G",
                     "S": "Z", "T": "N", "U": "P", "V": "Y", "W": "F", "X": "V", "Y": "O", "Z": "E"}

        self.notch = "F"
        self.double_stepping = "E"


class RotorIII(Rotor):
    def __init__(self, initial_position):
        Rotor.__init__(self, initial_position)
        self.ring = {"A": "B", "B": "D", "C": "F", "D": "H", "E": "J", "F": "L", "G": "C", "H": "P", "I": "R", "J": "T",
                     "K": "X", "L": "V", "M": "Z", "N": "N", "O": "Y", "P": "E", "Q": "I", "R": "W",
                     "S": "G", "T": "A", "U": "K", "V": "M", "W": "U", "X": "S", "Y": "Q", "Z": "O"}

        self.notch = "W"
        self.double_stepping = "V"


class RotorIV(Rotor):
    def __init__(self, initial_position):
        Rotor.__init__(self, initial_position)
        self.ring = {"A": "E", "B": "S", "C": "O", "D": "V", "E": "P", "F": "Z", "G": "J", "H": "A", "I": "Y", "J": "Q",
                     "K": "U", "L": "I", "M": "R", "N": "H", "O": "X", "P": "L", "Q": "N", "R": "F", "S": "T", "T": "G",
                     "U": "K", "V": "D", "W": "C", "X": "M", "Y": "W", "Z": "B"}

        self.notch = "K"
        self.double_stepping = "J"


class RotorV(Rotor):
    def __init__(self, initial_position):
        Rotor.__init__(self, initial_position)
        self.ring = {"A": "V", "B": "Z", "C": "B", "D": "R", "E": "G", "F": "I", "G": "T", "H": "Y", "I": "U", "J": "P",
                     "K": "S", "L": "D", "M": "N", "N": "H", "O": "L", "P": "X", "Q": "A", "R": "W", "S": "M", "T": "J",
                     "U": "Q", "V": "O", "W": "F", "X": "E", "Y": "C", "Z": "K"}

        self.notch = "A"
        self.double_stepping = "Z"
