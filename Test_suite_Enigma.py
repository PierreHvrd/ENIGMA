# this is the test suite for the ENIGMA project

from Enigma_Class import *
from Reflectors import *
from Rotors import *
from random import randint

rotor_1 = RotorIV("Q", "A")
rotor_2 = RotorII("E", "A")
rotor_3 = RotorI("K", "A")
reflector = ReflectorC()

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

enigma = Enigma(rotor_1, rotor_2, rotor_3, reflector, "")
text_cyphered = enigma.cypher("TZRBB RTCYJ AFGFW YWPNU SYVEZ KZAYQ VDZGJ PVPGY TLYQO GYIZM XPXUV IBKCC ")
print(text_cyphered)
assert text_cyphered == "ISUHS BHGEN TGSWS PSLFZ ZXYJK EHZWY SSYEY FANPK VWRTB IGVRU GDGFN TQRAR "

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


generate_test()
