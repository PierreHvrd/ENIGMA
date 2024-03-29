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

    def encrypt(self, plain_text):
        # first we have to remove the spaces and remove all the letters that are not from a to z and A to Z
        text_cleaned = ""
        plain_text.strip()
        for letter in plain_text:
            if 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122:
                text_cleaned += letter.upper()

        # then we actually encrypt the text
        text_encrypted = ""
        for letter in text_cleaned:
            # the rotors always rotate before the letter is encrypted and the third rotors rotate each time a letter
            # is encrypted

            # careful double step not counted
            self.rotor_3.rotate()
            if self.rotor_3.ring == self.rotor_2.notch:
                if self.rotor_2.ring == self.rotor_1.notch:
                    self.rotor_1.rotate()

                self.rotor_2.rotate()

            # Encryption: Plugboard -> 3 -> 2 -> 1 -> Reflector -> 1 -> 2 -> 3 -> Plugboard
            text_encrypted += self.rotor_3.encrypt(self.rotor_2.encrypt(self.rotor_1.encrypt(
                self.reflector.encrypt(
                    self.rotor_1.encrypt(self.rotor_2.encrypt(self.rotor_3.encrypt(letter)))))))

        return text_encrypted



