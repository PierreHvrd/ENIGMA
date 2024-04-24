# this is the main file that launches the graphic interface
import random
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Constants for the window
root_title = "ENIGMA M3 simulator"
WIDTH = 800
HIGH = 500
ICON = tk.PhotoImage(file="icon.png")
LINE_1 = 50  # first line of the application (where the reflector and the rotor selection is shown)
LINE_1_and_half = 85  # line where there are the position of the rotors
LINE_2 = 125  # line for the text of the plugboard
LINE_3 = 150  # line for the entry of the plugboard
LINE_4 = 200  # line for the randomize button, the save button and the load button
LINE_5 = 275  # line for the plaintext label and the cypher text label
LINE_6 = 300  # line for the two entry text (plain and cypher text)
LINE_7 = 370  # Line for the cypher button

# use the constants for the window
root.geometry(f"{WIDTH}x{HIGH}")
root.title(root_title)
root.resizable(False, False)  # to make the window not resizable
root.iconphoto(True, ICON)

# define all the labels
reflector_label = tk.Label(root, text="Reflector :")
rotor_1_type_label = tk.Label(root, text="Rotor 1 :")
rotor_2_type_label = tk.Label(root, text="Rotor 2 :")
rotor_3_type_label = tk.Label(root, text="Rotor 3 :")
rotor_1_position_label = tk.Label(root, text="Position: ")
rotor_2_position_label = tk.Label(root, text="Position: ")
rotor_3_position_label = tk.Label(root, text="Position: ")
plugboard_label = tk.Label(root, text="Plugboard: ")
plain_text_label = tk.Label(root, text="Plain text: ")
cypher_text_label = tk.Label(root, text="Cypher text: ")

# Drop down boxes

# reflector
reflector_options = ["B", "C"]
reflector_type = tk.StringVar()
reflector_type.set(reflector_options[0])
reflector_dropdown = tk.OptionMenu(root, reflector_type, *reflector_options)

# Rotors
rotors_options = ["I", "II", "III", "IV", "V"]
position_options = [chr(i) for i in range(65, 91)]  # a list with all the letters in the alphabet

# Rotor 1
rotor_1_type = tk.StringVar()
rotor_1_type.set(rotors_options[0])
rotor_1_type_dropdown = tk.OptionMenu(root, rotor_1_type, *rotors_options)

rotor_1_position_dropdown = ttk.Combobox(root, values=position_options, width=4)
rotor_1_position_dropdown.current(0)

# Rotor 2
rotor_2_type = tk.StringVar()
rotor_2_type.set(rotors_options[0])
rotor_2_dropdown = tk.OptionMenu(root, rotor_2_type, *rotors_options)

rotor_2_position_dropdown = ttk.Combobox(root, values=position_options, width=4)
rotor_2_position_dropdown.current(0)

# Rotor 3
rotor_3_type = tk.StringVar()
rotor_3_type.set(rotors_options[0])
rotor_3_dropdown = tk.OptionMenu(root, rotor_3_type, *rotors_options)

rotor_3_position_dropdown = ttk.Combobox(root, values=position_options, width=4)
rotor_3_position_dropdown.current(0)

# Entries and text boxes
plugboard_entry = tk.Entry(root, width=40)
plain_text_entry = tk.Text(root, width=30, height=10)
cypher_text_entry = tk.Text(root, width=30, height=10, state="disabled")

# commands


def randomize():
    # randomize the rotors sets
    rotor_1_type.set(rotors_options[random.randint(0, len(rotors_options) - 1)])
    rotor_2_type.set(rotors_options[random.randint(0, len(rotors_options) - 1)])
    rotor_3_type.set(rotors_options[random.randint(0, len(rotors_options) - 1)])

    # randomize positions
    rotor_1_position_dropdown.current(random.randint(0, len(position_options) - 1))
    rotor_2_position_dropdown.current(random.randint(0, len(position_options) - 1))
    rotor_3_position_dropdown.current(random.randint(0, len(position_options) - 1))

    # randomize the reflector type
    reflector_type.set(chr(random.randint(66, 67)))

    # randomize the plugboard
    alphabet = [chr(i) for i in range(65, 91)]
    nb_of_couples = random.randint(0, 13)
    couples = ""
    for j in range(nb_of_couples):
        first_letter_of_couple = random.randint(0, len(alphabet) - 1)
        couples += alphabet[first_letter_of_couple]
        alphabet.pop(first_letter_of_couple)

        second_letter_of_the_couple = random.randint(0, len(alphabet) - 1)
        couples += alphabet[second_letter_of_the_couple]
        alphabet.pop(second_letter_of_the_couple)

        couples += " "

    plugboard_entry.delete(0, "end")
    plugboard_entry.insert(0, couples)



# Buttons
randomize_button = tk.Button(root, text="Randomize", command=randomize)
save_button = tk.Button(root, text="Save")
load_button = tk.Button(root, text="Load")
cypher_button = tk.Button(root, text="Cypher")


# place all the elements
reflector_label.place(x=100, y=LINE_1)
reflector_dropdown.place(x=165, y=LINE_1)

rotor_1_type_label.place(x=250, y=LINE_1)
rotor_1_type_dropdown.place(x=300, y=LINE_1)
rotor_1_position_label.place(x=250, y=LINE_1_and_half)
rotor_1_position_dropdown.place(x=305, y=LINE_1_and_half)

rotor_2_type_label.place(x=400, y=LINE_1)
rotor_2_dropdown.place(x=450, y=LINE_1)
rotor_2_position_label.place(x=400, y=LINE_1_and_half)
rotor_2_position_dropdown.place(x=455, y=LINE_1_and_half)

rotor_3_type_label.place(x=550, y=LINE_1)
rotor_3_dropdown.place(x=600, y=LINE_1)
rotor_3_position_label.place(x=550, y=LINE_1_and_half)
rotor_3_position_dropdown.place(x=605, y=LINE_1_and_half)

plugboard_label.place(x=350, y=LINE_2)
plugboard_entry.place(x=265, y=LINE_3)

randomize_button.place(x=100, y=LINE_4)
save_button.place(x=375, y=LINE_4)
load_button.place(x=625, y=LINE_4)
cypher_button.place(x=385, y=LINE_7)

plain_text_label.place(x=100, y=LINE_5)
plain_text_entry.place(x=100, y=LINE_6)


cypher_text_label.place(x=475, y=LINE_5)
cypher_text_entry.place(x=475, y=LINE_6)

# finally, we launch the mainloop
root.mainloop()
