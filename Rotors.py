# file where all the rotors are defined
from abc import ABC, abstractmethod


class Rotor(ABC):
    """
    Careful with the following difference
    Type of the rotor: I-II-III-IV-V
    Physical emplacement of the rotor in the machine: 1-2-3
    """
    @abstractmethod
    def __init__(self, initial_position: str, ring_setting: str):
        self.position = initial_position  # capital letter
        self.ring_setting = ring_setting
        self.ring = {}
        self.notch = ""  # when this letter is reached the next rotor has to rotate
        self.double_stepping = ""  # when this position is reached BY THE MIDDLE ROTOR it rotates again and make the
        # next rotate this position is always the position before the notch position.

    def rotate(self):
        self.position = chr(ord(self.position) + 1)
        if ord(self.position) > 90:
            self.position = "A"

    def cypher(self, letter):
        """
        Everything is this function is done with number (ascii codes of the letters) because it is
        simpler for the calculations
        """
        """
        # first we apply the ring setting
        encryption = ord(letter) - ord(self.ring_setting) + 65

        if encryption < 65:
            encryption += 26
        """

        # first we apply the position of the rotor
        encryption = self.cesar_cypher(letter, True)

        for key in self.ring.keys():
            if key == chr(encryption):
                encryption = ord(self.ring[key])
                break

        """
        # finally we apply the ring setting again but reversed
        encryption = encryption + ord(self.ring_setting) - 65

        if encryption > 90:
            encryption -= 26  # in the case we look back ex: A -> Z (with ring setting "B")
        """

        # finally we apply the position of the rotor to the output
        encryption = self.cesar_cypher(chr(encryption), False)

        return chr(encryption)

    def cypher_back(self, letter):
        """
        Everything is this function is done with number (ascii codes of the letters) because it is
        simpler for the calculations.
        This is the reciprocal function of cypher.
        """
        """
        # first we apply the ring setting
        encryption = ord(letter) - ord(self.ring_setting) + 65

        if encryption < 65:
            encryption += 26
        """

        # first we apply the position of the rotor
        encryption = self.cesar_cypher(letter, True)

        for key, value in self.ring.items():
            if value == chr(encryption):
                encryption = ord(key)
                break

        """
        # finally we apply the ring setting again but reversed
        encryption = encryption + ord(self.ring_setting) - 65

        if encryption > 90:
            encryption -= 26  # in the case we look back ex: A -> Z (with ring setting "B")
        """

        # finally we apply the position of the rotor to the output
        # first we apply the position of the rotor
        encryption = self.cesar_cypher(chr(encryption), False)

        return chr(encryption)

    def cesar_cypher(self, letter, plus):
        """
        Useful to apply the position of the rotor.
        :param letter:
        :param plus: a boolean that tells if the cypher is positive (A -> B, B-> C) or negative (B-> A, C-> B)
        :return:
        """
        if plus:
            cypher = (ord(letter) - 65 + ord(self.position) - 65) % 26
            return cypher + 65
        else:
            cypher = (ord(letter) - 65 - (ord(self.position) - 65)) % 26
            return cypher + 65

    def print_state(self, rotor_number):
        print(f"State of the Rotor {rotor_number}:\nPosition: {self.position}\nRing: {self.ring}")


class RotorI(Rotor):
    def __init__(self, initial_position, ring_setting):
        Rotor.__init__(self, initial_position, ring_setting)
        self.ring = {"A": "E", "B": "K", "C": "M", "D": "F", "E": "L", "F": "G", "G": "D", "H": "Q", "I": "V", "J": "Z",
                     "K": "N", "L": "T", "M": "O", "N": "W", "O": "Y", "P": "H", "Q": "X", "R": "U",
                     "S": "S", "T": "P", "U": "A", "V": "I", "W": "B", "X": "R", "Y": "C", "Z": "J"}

        self.notch = "R"
        self.double_stepping = "Q"
        """
        self.notch = chr(ord("R") + ord(self.ring_setting) - 65)  # we set the notch (Q for this rotor)
        # and adjust it with the ring setting
        """


class RotorII(Rotor):
    def __init__(self, initial_position, ring_setting):
        Rotor.__init__(self, initial_position, ring_setting)
        self.ring = {"A": "A", "B": "J", "C": "D", "D": "K", "E": "S", "F": "I", "G": "R", "H": "U", "I": "X", "J": "B",
                     "K": "L", "L": "H", "M": "W", "N": "T", "O": "M", "P": "C", "Q": "Q", "R": "G",
                     "S": "Z", "T": "N", "U": "P", "V": "Y", "W": "F", "X": "V", "Y": "O", "Z": "E"}

        self.notch = "F"
        self.double_stepping = "E"
        """
        self.notch = chr(ord("R") + ord(self.ring_setting) - 65)  # we set the notch (Q for this rotor)
        # and adjust it with the ring setting
        """


class RotorIII(Rotor):
    def __init__(self, initial_position, ring_setting):
        Rotor.__init__(self, initial_position, ring_setting)
        self.ring = {"A": "B", "B": "D", "C": "F", "D": "H", "E": "J", "F": "L", "G": "C", "H": "P", "I": "R", "J": "T",
                     "K": "X", "L": "V", "M": "Z", "N": "N", "O": "Y", "P": "E", "Q": "I", "R": "W",
                     "S": "G", "T": "A", "U": "K", "V": "M", "W": "U", "X": "S", "Y": "Q", "Z": "O"}

        self.notch = "W"
        self.double_stepping = "V"

        """
        self.notch = chr(ord("R") + ord(self.ring_setting) - 65)  # we set the notch (Q for this rotor)
        # and adjust it with the ring setting
        """


class RotorIV(Rotor):
    def __init__(self, initial_position, ring_setting):
        Rotor.__init__(self, initial_position, ring_setting)
        self.ring = {"A": "E", "B": "S", "C": "O", "D": "V", "E": "P", "F": "Z", "G": "J", "H": "A", "I": "Y", "J": "Q",
                     "K": "U", "L": "I", "M": "R", "N": "H", "O": "X", "P": "L", "Q": "N", "R": "F", "S": "T", "T": "G",
                     "U": "K", "V": "D", "W": "C", "X": "M", "Y": "W", "Z": "B"}

        self.notch = "K"
        self.double_stepping = "J"
        """
        self.notch = chr(ord("R") + ord(self.ring_setting) - 65)  # we set the notch (Q for this rotor)
        # and adjust it with the ring setting
        """


class RotorV(Rotor):
    def __init__(self, initial_position, ring_setting):
        Rotor.__init__(self, initial_position, ring_setting)
        self.ring = {"A": "V", "B": "Z", "C": "B", "D": "R", "E": "G", "F": "I", "G": "T", "H": "Y", "I": "U", "J": "P",
                     "K": "S", "L": "D", "M": "N", "N": "H", "O": "L", "P": "X", "Q": "A", "R": "W", "S": "M", "T": "J",
                     "U": "Q", "V": "O", "W": "F", "X": "E", "Y": "C", "Z": "K"}

        self.notch = "A"
        self.double_stepping = "Z"
        """
        self.notch = chr(ord("R") + ord(self.ring_setting) - 65)  # we set the notch (Q for this rotor)
        # and adjust it with the ring setting
        """
