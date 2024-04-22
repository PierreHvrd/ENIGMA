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
        