# this is the test suite for the ENIGMA project

from Classes.Enigma_Class import *
from Classes.Reflectors import *
from Classes.Rotors import *

rotor_1 = RotorI("H", "A")
rotor_2 = RotorII("F", "A")
rotor_3 = RotorIII("U", "A")
reflector = ReflectorB()

enigma_machine = Enigma(rotor_1, rotor_2, rotor_3, reflector, "")

print(enigma_machine.encrypt("This is a relatable text to encrypt"))
