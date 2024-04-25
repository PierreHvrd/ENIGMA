# this file contains the code for the enigma class
from Rotor_abstract import Rotor
from Reflector_abstract import Reflector


class Enigma:
    def __init__(self, rotor_1: Rotor, rotor_2: Rotor, rotor_3: Rotor, reflector: Reflector, plugboard_state):
        self.rotor_1 = rotor_1
        self.rotor_2 = rotor_2
        self.rotor_3 = rotor_3
        self.reflector = reflector
        self.plugboard = {}

        # then we create the dict representing the plugboard state
        self.init_good = self.build_plugboard(plugboard_state)

    def build_plugboard(self, plugboard_state):
        """
        This functions converts a string like this 'AB CD ' into a dictionary like this: {'A':'B', 'C':'D'}.
        The letters can be uppercase or lowercase. And there can be multiple spaces between the letter (not only one).
        However, if there are no spaces between the letters or non-ascii characters the method won't work
        :param plugboard_state: A string like this 'Ab Cd   ef' should only contain upper or lowercase letters and
        spaces
        :returns: A boolean, true if everything went good, false otherwise
        """
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

                    if previous_char == plugboard_state[i]:
                        correct_format = False

                    if correct_format:
                        dict_plugboard[previous_char] = plugboard_state[i]

            previous_char = plugboard_state[i]

            i += 1
        if correct_format:
            self.plugboard = dict_plugboard
            return True

        else:
            # the format is wrong: display something
            return False

    def cypher(self, plain_text):
        """
        This method return the letter cyphered after the whole encryption process. The encryption process contains the
         plugboard, the three rotors and the reflector
        :param plain_text: A string, it can contain non-ascii characters, but they will be ignored. The spaces are also
        ignored
        :return: text_cyphered : A string that contains only upper letters and spaces. Every 5 characters there is a
        space to make the string more readable.
        """
        # first we have to remove the spaces and remove all the letters that are not from a to z and A to Z
        text_cleaned = self.clean_text(plain_text)

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

            text_cyphered += plugboard_backward_cypher
            # we add spaces every 5 character to make it more readable
            text_length += 1
            if text_length % 5 == 0 and text_length != 0:
                text_cyphered += " "

        return text_cyphered

    def clean_text(self, plain_text):
        """
        This method just selects the upper and lower letters in the text and turn the lower letters into upper letters
        :param plain_text: str
        :return: text_cleaned text that contains only upper letters and spaces
        """
        text_cleaned = ""
        plain_text.strip()
        for letter in plain_text:
            if 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122:
                text_cleaned += letter.upper()

        return text_cleaned

    def plugboard_cypher(self, letter):
        """
        This functions returns the letter passed in parameters or, if the letter passed in parameters is plugged to
        another then it return the other letter
        :param letter: string of length 1
        :return: letter: string of length 1
        """
        for key, value in self.plugboard.items():
            if letter == key:
                return value

            elif letter == value:
                return key

        return letter
