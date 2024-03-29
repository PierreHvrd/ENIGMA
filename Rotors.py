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
        self.ring = []
        self.notch = ""  # when this letter is reached the rotors has to rotate

    def rotate(self):
        self.ring.append(self.ring.pop(0))
        self.position = chr(ord(self.position) + 1)
        if ord(self.position) > 90:
            self.position = "A"

    def set_in_position(self, initial_position):
        for i in range(ord(initial_position) - 65):
            self.ring.append(self.ring.pop(0))

    def encrypt(self, letter):
        """
        Everything is this function is done with number (ascii codes of the letters) because it is
        simpler for the calculations
        """
        # first we apply the ring setting
        encryption = ord(letter) - ord(self.ring_setting) + 65

        if encryption < 65:
            encryption += 26

        """
        # then we apply the position of the rotor
        encryption = encryption + ord(self.position) - 65
        """
        if encryption > 90:
            encryption -= 26

        encryption = ord(self.ring[encryption - 65])

        # finally we apply the ring setting again but reversed
        encryption = encryption + ord(self.ring_setting) - 65

        if encryption > 90:
            encryption -= 26  # in the case we look back ex: A -> Z (with ring setting "B")

        encryption = encryption - ord(self.position) + 65
        if encryption < 65:
            encryption += 26  # in the case we look back ex: A -> Z (with ring setting "B")

        return chr(encryption)

    def print_state(self, rotor_number):
        print(f"State of the Rotor {rotor_number}:\nPosition: {self.position}\nRing: {self.ring}")


class RotorI(Rotor):
    def __init__(self, initial_position, ring_setting):
        Rotor.__init__(self, initial_position, ring_setting)
        self.ring = ["E", "K", "M", "F", "L", "G", "D", "Q", "V", "Z", "N", "T", "O", "W", "Y", "H", "X", "U",
                     "S", "P", "A", "I", "B", "R", "C", "J"]

        # put the encryption in the correct position
        self.set_in_position(initial_position)

        self.notch = chr(ord("Q") + ord(self.ring_setting) - 65)  # we set the notch (Q for this rotor)
        # and adjust it with the ring setting


class RotorII(Rotor):
    def __init__(self, initial_position, ring_setting):
        Rotor.__init__(self, initial_position, ring_setting)
        self.ring = ["A", "J", "D", "K", "S", "I", "R", "U", "X", "B", "L", "H", "W", "T", "M", "C", "Q", "G", "Z", "N",
                     "P", "Y", "F", "V", "O", "E"]

        # put the encryption in the correct position
        self.set_in_position(initial_position)

        self.notch = chr(ord("E") + ord(self.ring_setting) - 65)


class RotorIII(Rotor):
    def __init__(self, initial_position, ring_setting):
        Rotor.__init__(self, initial_position, ring_setting)
        self.ring = ["B", "D", "F", "H", "J", "L", "C", "P", "R", "T", "X", "V", "Z", "N", "Y", "E", "I", "W", "G", "A",
                     "K", "M", "U", "S", "Q", "O"]

        # put the encryption in the correct position
        self.set_in_position(initial_position)

        self.notch = chr(ord("V") + ord(self.ring_setting) - 65)


class RotorIV(Rotor):
    def __init__(self, initial_position, ring_setting):
        Rotor.__init__(self, initial_position, ring_setting)
        self.ring = ["E", "S", "O", "V", "P", "Z", "J", "A", "Y", "Q", "U", "I", "R", "H", "X", "L", "N", "F", "T", "G",
                     "K", "D", "C", "M", "W", "B"]

        # put the encryption in the correct position
        self.set_in_position(initial_position)

        self.notch = chr(ord("J") + ord(self.ring_setting) - 65)


class RotorV(Rotor):
    def __init__(self, initial_position, ring_setting):
        Rotor.__init__(self, initial_position, ring_setting)
        self.ring = ["V", "Z", "B", "R", "G", "I", "T", "Y", "U", "P", "S", "D", "N", "H", "L", "X", "A", "W", "M", "J",
                     "Q", "O", "F", "E", "C", "K"]

        # put the encryption in the correct position
        self.set_in_position(initial_position)

        self.notch = chr(ord("Z") + ord(self.ring_setting) - 65)

