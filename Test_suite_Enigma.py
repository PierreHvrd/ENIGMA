# this is the test suite for the ENIGMA project

from Enigma_Class import *
from Reflectors import *
from Rotors import *

rotor_1 = RotorII("Z", "A")

for i in range(10):
    rotor_1.rotate()
    print(f"Letter encrypted: {rotor_1.encrypt('A')}")

