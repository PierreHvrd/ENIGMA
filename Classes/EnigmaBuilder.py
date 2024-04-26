# this file contains the code for the EnigmaBuilder

from .Rotors.RotorI import RotorI
from .Rotors.RotorII import RotorII
from .Rotors.RotorIII import RotorIII
from .Rotors.RotorIV import RotorIV
from .Rotors.RotorV import RotorV
from .Reflectors.ReflectorB import ReflectorB
from .Reflectors.ReflectorC import ReflectorC
from .Enigma_Class import Enigma


class EnigmaBuilder:
    def __init__(self):
        self.rotor_1 = None
        self.rotor_2 = None
        self.rotor_3 = None
        self.reflector = None
        self.plugboard = {}
        self.dict_to_instantiate = {"RotorI": RotorI, "RotorII": RotorII, "RotorIII": RotorIII, "RotorIV": RotorIV,
                                    "RotorV": RotorV,
                                    "B": ReflectorB, "C": ReflectorC}
        self.build_ok = True

    def set_rotor(self, nb_of_the_rotor, type_of_the_rotor, position_of_the_rotor):
        rotor_name = f"Rotor{type_of_the_rotor}"
        if nb_of_the_rotor == 1:
            self.rotor_1 = self.dict_to_instantiate[rotor_name](position_of_the_rotor)

        elif nb_of_the_rotor == 2:
            self.rotor_2 = self.dict_to_instantiate[rotor_name](position_of_the_rotor)

        else:
            self.rotor_3 = self.dict_to_instantiate[rotor_name](position_of_the_rotor)

        return self

    def set_reflector(self, reflector_type):
        self.reflector = self.dict_to_instantiate[reflector_type]()
        return self

    def set_plugboard(self, plugboard_state):
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

        self.build_ok = correct_format
        if correct_format:
            self.plugboard = dict_plugboard

        return self

    def build(self):
        return Enigma(self)
