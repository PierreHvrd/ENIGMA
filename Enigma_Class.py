# this file contains the code for the enigma class
from Rotors import Rotor
from Reflectors import Reflector


class Enigma:
    def __init__(self, rotor_1: Rotor, rotor_2: Rotor, rotor_3: Rotor, reflector: Reflector, plugboard_state):
        self.rotor_1 = rotor_1
        self.rotor_2 = rotor_2
        self.rotor_3 = rotor_3
        self.reflector = reflector
        self.plugboard = {}

        # then we create the dict representing the plugboard state
        self.build_plugboard(plugboard_state)

    def build_plugboard(self, plugboard_state):
        # first we remove the double (or more) spaces
        pre_treatment = ""
        plugboard_state_length = len(plugboard_state)
        previous_letter = " "  # important to remove the spaces at the beginning of the string
        j = 0
        while j < plugboard_state_length:
            if previous_letter != " " or plugboard_state[j] != " ":
                pre_treatment += plugboard_state[j]

            previous_letter = plugboard_state[j]
            j += 1

        plugboard_state = pre_treatment

        # then we convert everything to upper
        plugboard_state = plugboard_state.upper()
        plugboard_state_length = len(plugboard_state)
        correct_format = True
        dict_plugboard = {}

        # we check that there are only letters and spaces
        i = 0
        previous_char = " "
        while correct_format and i < plugboard_state_length:
            code_ascii_letter = ord(plugboard_state[i])

            # plugboard_state must contain only letters and spaces
            if (code_ascii_letter > 90 or code_ascii_letter < 65) and code_ascii_letter != 32:
                correct_format = False

            # we check that if the current char is a space it is between two letters
            elif code_ascii_letter == 32:
                if (i + 1) % 3 != 0:
                    correct_format = False

            else:
                if previous_char != " ":
                    # we check that both letters of the pair are free
                    for pair in dict_plugboard.items():
                        if previous_char in pair or plugboard_state[i] in pair:
                            correct_format = False  # one letter can only be swapped with another, not two others

                    if correct_format:
                        dict_plugboard[previous_char] = plugboard_state[i]

            previous_char = plugboard_state[i]

            i += 1
        if correct_format:
            self.plugboard = dict_plugboard

        else:
            # the format is wrong: display something
            print("The format of the string is incorrect")

    def print_state(self):
        print(f"Plugboard state: {self.plugboard}")
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
            plugboard_forward_cypher = self.plugboard_cypher(letter)
            rotor3_cypher = self.rotor_3.cypher(plugboard_forward_cypher)
            rotor2_cypher = self.rotor_2.cypher(rotor3_cypher)
            rotor1_cypher = self.rotor_1.cypher(rotor2_cypher)

            # reflection
            reflector_cypher = self.reflector.cypher(rotor1_cypher)
            rotor1_cypher_back = self.rotor_1.cypher_back(reflector_cypher)
            rotor2_cypher_back = self.rotor_2.cypher_back(rotor1_cypher_back)
            rotor3_cypher_back = self.rotor_3.cypher_back(rotor2_cypher_back)
            plugboard_backward_cypher = self.plugboard_cypher(rotor3_cypher_back)
            """text_cyphered += self.rotor_3.cypher(self.rotor_2.cypher(self.rotor_1.cypher(
                self.reflector.cypher(
                    self.rotor_1.cypher(self.rotor_2.cypher(self.rotor_3.cypher(letter)))))))
            """
            text_cyphered += plugboard_backward_cypher
            # we add spaces every 5 character to make it more readable
            text_length += 1
            if text_length % 5 == 0 and text_length != 0:
                text_cyphered += " "

        return text_cyphered

    def plugboard_cypher(self, letter):
        for key, value in self.plugboard.items():
            if letter == key:
                return value

            elif letter == value:
                return key

        return letter
