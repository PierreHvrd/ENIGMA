# this is the test suite for the ENIGMA project

from Enigma_Class import *
from ReflectorB import ReflectorB
from ReflectorC import ReflectorC
from random import randint
from RotorI import RotorI
from RotorII import RotorII
from RotorIII import RotorIII
from RotorIV import RotorIV
from RotorV import RotorV

rotor_1 = RotorIII("N")
rotor_2 = RotorI("K")
rotor_3 = RotorV("M")
rotor_4 = RotorIV("O")
rotor_5 = RotorV("Q")
reflectorB = ReflectorB()  # strategy
reflectorC = ReflectorC()

"""
# just test that the rotor rotates correctly
rotor_1_bis = RotorI("Z", "A")
text = ""
for i in range(7):
    rotor_1_bis.rotate()
    text += rotor_1_bis.cypher("A")

assert text == "EJKCHBX"

rotor_2_bis = RotorII("Z", "A")
text = ""
for i in range(7):
    rotor_2_bis.rotate()
    text += rotor_2_bis.cypher("A")

assert text == "AIBHODL"
"""

enigma = Enigma(rotor_1, rotor_2, rotor_3, reflectorC, "")
enigma_2 = Enigma(rotor_5, rotor_3, rotor_1, "")
print(enigma_2 == enigma)

text_encrypted = enigma.cypher("OSKQH SHAWU SOAMA GVBIW OWBOM ENCBN HHEUE WQQBW VGSTN CABBW MOARS CLQPH V")
# text_encrypted_2 = enigma_2.cypher("OSKQH SHAWU SOAMA GVBIW OWBOM ENCBN HHEUE WQQBW VGSTN CABBW MOARS CLQPH V")
print(text_encrypted)
assert text_encrypted == "MQLEI IKFYA TQLSO BJJHM IPZRU SWOSK ZVFOR PUBQH QALZI SJRVD NHTUD HUJAQ L"
# assert text_encrypted == text_encrypted_2


def generate_test():

    for i in range(1, 4):
        print(f"Rotor n°{i}: {randint(1, 5)}")
        print(f"Position: {chr(randint(65, 90))}\n")

    reflector_B_or_C = randint(1, 2)
    if reflector_B_or_C == 1:
        print("Reflector : B")

    else:
        print("Reflector : C")

    text = ""
    for i in range(1, randint(20, 100)):
        text += chr(randint(65, 90))

        if i % 5 == 0:
            text += " "

    print(text)


# generate_test()
"""
enigma_instance_1 = Enigma()
enigma_instance_2 = Enigma()

singleton_instance_1.set_value(42)
print(singleton_instance_2.get_value())


singleton_instance_2.set_value(123)
print(singleton_instance_1.get_value())


singleton_instance_1.set_value(1, firstname="Rick", lastname="Sanchez", age=70)
print(singleton_instance_1.get_param_value("firstname"))
print(singleton_instance_2.get_param_value("lastname"))
print(singleton_instance_1 is singleton_instance_2)
"""