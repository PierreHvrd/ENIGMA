# this file contains the code for the enigma class
from Rotors import Rotor
from Reflectors import Reflector


class Enigma:
    def __init__(self, rotor_1: Rotor, rotor_2: Rotor, rotor_3: Rotor, reflector: Reflector, plugboard_state):
        self.rotor_1 = rotor_1
        self.rotor_2 = rotor_2
        self.rotor_3 = rotor_3
        self.reflector = reflector
        self.plugboard_state = plugboard_state

    def print_state(self):
        print(f"Plugboard state: {self.plugboard_state}")
        self.rotor_1.print_state(1)
        self.rotor_2.print_state(2)
        self.rotor_3.print_state(3)
        self.reflector.print_type()

    def cypher(self, plain_text):
        # first we have to remove the spaces and remove all the letters that are not from a to z and A to Z
        text_cleaned = ""
        plain_text.strip()
        for letter in plain_text:
            if 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122:
                text_cleaned += letter.upper()

        # then we actually encrypt the text
        text_cyphered = ""
        text_length = 0
        for letter in text_cleaned:
            # the rotors always rotate before the letter is encrypted and the third rotors rotate each time a letter
            # is encrypted

            # first we rotate the rotors
            self.rotor_3.rotate()

            if self.rotor_3.position == self.rotor_3.notch:
                self.rotor_2.rotate()
                if self.rotor_2.position == self.rotor_2.notch:
                    self.rotor_1.rotate()

            # double stepping
            if self.rotor_2.position == self.rotor_2.double_stepping and self.rotor_3.position != self.rotor_3.notch:
                # the second condition is important because it is important that the middle rotor does not rotate
                # two times with just one keystroke on the keyboard
                self.rotor_2.rotate()
                self.rotor_1.rotate()

            # Encryption: Plugboard -> 3 -> 2 -> 1 -> Reflector -> 1 -> 2 -> 3 -> Plugboard

            # forward pass
            rotor3_cypher = self.rotor_3.cypher(letter)
            rotor2_cypher = self.rotor_2.cypher(rotor3_cypher)
            rotor1_cypher = self.rotor_1.cypher(rotor2_cypher)

            # reflection
            reflector_cypher = self.reflector.cypher(rotor1_cypher)
            rotor1_cypher_back = self.rotor_1.cypher_back(reflector_cypher)
            rotor2_cypher_back = self.rotor_2.cypher_back(rotor1_cypher_back)
            rotor3_cypher_back = self.rotor_3.cypher_back(rotor2_cypher_back)
            """text_cyphered += self.rotor_3.cypher(self.rotor_2.cypher(self.rotor_1.cypher(
                self.reflector.cypher(
                    self.rotor_1.cypher(self.rotor_2.cypher(self.rotor_3.cypher(letter)))))))
            """
            text_cyphered += rotor3_cypher_back
            # we add spaces every 5 character to make it more readable
            text_length += 1
            if text_length % 5 == 0 and text_length != 0:
                text_cyphered += " "

        return text_cyphered



