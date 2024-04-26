# this is the test suite for the ENIGMA project

import unittest
from Classes.EnigmaBuilder import EnigmaBuilder
from Classes.Rotors.RotorI import RotorI
from Classes.Rotors.RotorII import RotorII
from Classes.Rotors.RotorIII import RotorIII
from Classes.Rotors.RotorIV import RotorIV
from Classes.Rotors.RotorV import RotorV
from Classes.Reflectors.ReflectorB import ReflectorB


class TestEnigma(unittest.TestCase):
    def setUp(self):
        # rotors for individual tests
        self.rotor_I_E = RotorI("E")
        self.rotor_II_I = RotorII("I")
        self.rotor_III_T = RotorIII("T")
        self.rotor_III_K = RotorIII("K")
        self.rotor_IV_S = RotorIV("S")
        self.rotor_V_C = RotorV("C")

        # reflector for individual tests
        self.reflector_B = ReflectorB()

        # enigma machine to test the whole machine
        self.enigma_builder = EnigmaBuilder()
        self.enigma_builder = self.enigma_builder.set_rotor(1, "I", "Z")
        self.enigma_builder = self.enigma_builder.set_rotor(2, "IV", "R")
        self.enigma_builder = self.enigma_builder.set_rotor(3, "III", "T")
        self.enigma_builder = self.enigma_builder.set_reflector("C")
        self.enigma_builder = self.enigma_builder.set_plugboard("TI GV FR UC MH QY SW JP BL ZO")
        self.enigma = self.enigma_builder.build()
        self.text = "ours is the Earth and everything that’s in it, And—which is more—you’ll be a Man, my son!"

    def test_rotors(self):
        self.assertEqual(self.rotor_I_E.cypher("K"), "U")
        self.assertEqual(self.rotor_II_I.cypher("M"), "H")
        self.assertEqual(self.rotor_III_K.cypher("J"), "Q")
        self.assertEqual(self.rotor_IV_S.cypher("D"), "L")
        self.assertEqual(self.rotor_V_C.cypher("S"), "O")

    def test_reflector(self):
        self.assertEqual(self.reflector_B.cypher("M"), "O")
        self.assertEqual(self.reflector_B.cypher("E"), "Q")
        self.assertEqual(self.reflector_B.cypher("N"), "K")

    def test_all_enigma_machine(self):
        self.assertEqual(self.enigma.cypher(self.text), "KHMEG QYWYD SZCJU JZDRI OPVBS XRLRW NZQLC KODYO EZZMB TJYSX"
                                                        " SKARI FHBZM GHPFH L")  # result verified by multiples online
        # emulators


unittest.main()
