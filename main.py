import random
from locations import locations
from motivations import motivations
from suspects import suspects
from tkinter import *


game_over = False
# take incorrect guesses and give player option what to do with them
# Offer rewards for actions (help player zero in on corect answer)
# based on actions taken alter ending (exterminatus/benevolence)
incorrect_location_accusations = []
incorrect_suspect_accusations = []
incorrect_motivation_accusations = []

heresy_limit = random.randint(10, 15)
total_heresy = 0

# randomly select a heretic, a location and a motivation
suspect_solution = random.choice(suspects)
location_solution = random.choice(locations)
motivation_solution = random.choice(motivations)

game_solution = [suspect_solution["number_ID"], location_solution["number_ID"], motivation_solution["number_ID"]]


def suspect_radio_used():
    suspect_radio_state.get()


def location_radio_used():
    location_radio_state.get()


def motivation_radio_used():
    motivation_radio_state.get()


def submit_accusation():
    accused_suspect = suspect_radio_state.get()
    if accused_suspect != game_solution[0]:
        if accused_suspect in incorrect_suspect_accusations:
            pass
        else:
            incorrect_suspect_accusations.append(accused_suspect)
            print(f"wrong suspects: {incorrect_suspect_accusations}")
    accused_location = location_radio_state.get()
    if accused_location != game_solution[1]:
        if accused_location in incorrect_location_accusations:
            pass
        else:
            incorrect_location_accusations.append(accused_location)
            print(f"wrong locations: {incorrect_location_accusations}")
    accused_motivation = motivation_radio_state.get()
    if accused_motivation != game_solution[2]:
        if accused_motivation in incorrect_motivation_accusations:
            pass
        else:
            incorrect_motivation_accusations.append(accused_motivation)
            print(f"wrong motivations: {incorrect_motivation_accusations}")
    answer = [accused_suspect, accused_location, accused_motivation]
    if answer == game_solution:
        print("BINGO!!!!")
    if accused_suspect == game_solution[0]:
        name = suspects[accused_suspect - 1]["name"]
        print(f"The Heretic is {name}!")
    if accused_location == game_solution[1]:
        name = locations[accused_location - 1]["name"]
        print(f"There is heresy at the {name}!")
    if accused_motivation == game_solution[2]:
        name = motivations[accused_motivation - 1]["name"]
        print(f"The foul stench of {name} is clearly the cause of this heresy")


# print locations to visit
def display_locations():
    """Displays locations and their ID numbers for user to reference. Will update list as accusations are made"""
    location_window = Toplevel(window)
    location_window.title("Locations")
    location_window.geometry("200x200")
    location_window.config(pady=25)
    for location in locations:
        location_id = location["number_ID"]
        if location_id in incorrect_location_accusations:
            pass
        else:
            location_name = location["name"]
            location_label = Label(location_window, text=f"{location_id}: {location_name}")
            location_label.pack()


# print suspects to accuse
def display_suspects():
    """Displays suspects and their ID numbers for user to reference. Will update list as accusations are made"""
    suspect_window = Toplevel(window)
    suspect_window.title("Suspects")
    suspect_window.geometry("200x200")
    suspect_window.config(pady=25)
    for suspect in suspects:
        suspect_id = suspect["number_ID"]
        if suspect_id in incorrect_suspect_accusations:
            pass
        else:
            suspect_name = suspect["name"]
            suspect_label = Label(suspect_window, text=f"{suspect_id}: {suspect_name}")
            suspect_label.pack()


# print motivations
def display_motivations():
    """Displays motivations and their ID numbers for user to reference. Will update list as accusations are made"""
    motivation_window = Toplevel(window)
    motivation_window.title("Motivations")
    motivation_window.geometry("200x200")
    motivation_window.config(pady=25)
    for motivation in motivations:
        motivation_id = motivation["number_ID"]
        if motivation_id in incorrect_motivation_accusations:
            pass
        else:
            motivation_name = motivation["name"]
            motivation_label = Label(motivation_window, text=f"{motivation_id}: {motivation_name}")
            motivation_label.pack()


# displays locations, suspects and motivations
def notebook():
    display_suspects()
    display_locations()
    display_motivations()


def make_accusation():
    accusation_window = Toplevel(window)
    accusation_window.geometry("550x275")
    accusation_window.title("Accusation")
    accusation_window.config(pady=25)
    suspect_label = Label(accusation_window, text="Suspects")
    suspect_label.grid(column=0, row=0)
    location_label = Label(accusation_window, text="Locations")
    location_label.grid(column=1, row=0)
    motivation_label = Label(accusation_window, text="Motivations")
    motivation_label.grid(column=2, row=0)
    suspect_value = 1
    motivation_value = 1
    location_value = 1
    for suspect in suspects:
        suspect_name = suspect["name"]
        suspect_id = suspect["number_ID"]
        suspect_radiobutton = Radiobutton(accusation_window,
                                          text=f"{suspect_id}: {suspect_name}",
                                          value=suspect_value,
                                          variable=suspect_radio_state,
                                          command=suspect_radio_used)
        suspect_radiobutton.config(padx=20)
        suspect_radiobutton.grid(column=0, row=suspect_value)
        suspect_value += 1
    for location in locations:
        location_name = location["name"]
        location_id = location["number_ID"]
        location_radiobutton = Radiobutton(accusation_window,
                                           text=f"{location_id}: {location_name}",
                                           value=location_value,
                                           variable=location_radio_state,
                                           command=location_radio_used)
        location_radiobutton.config(padx=20)
        location_radiobutton.grid(column=1, row=location_value)
        location_value += 1
    for motivation in motivations:
        motivation_name = motivation["name"]
        motivation_id = motivation["number_ID"]
        motivation_radiobutton = Radiobutton(accusation_window,
                                             text=f"{motivation_id}: {motivation_name}",
                                             value=motivation_value,
                                             variable=motivation_radio_state,
                                             command=motivation_radio_used)
        motivation_radiobutton.config(padx=20)
        motivation_radiobutton.grid(column=2, row=motivation_value)
        motivation_value += 1

    confirm_button = Button(accusation_window, text="Submit Accusation", command=submit_accusation)
    confirm_button.grid(column=0, row=9, columnspan=3)


window = Tk()
window.title("Hereticus")
window.geometry('500x500')

accusation_button = Button(text="Make Accusation", command=make_accusation)
accusation_button.pack()

check_suspects_button = Button(text="List of Suspects", command=display_suspects)
check_suspects_button.pack()

check_location_button = Button(text="List of Locations", command=display_locations)
check_location_button.pack()

check_motivation_button = Button(text="List of Motives", command=display_motivations)
check_motivation_button.pack()

current_heresy_label = Label(text=f"Heresy Level: {total_heresy}")
current_heresy_label.pack()

suspect_radio_state = IntVar()
motivation_radio_state = IntVar()
location_radio_state = IntVar()

print(game_solution)

window.mainloop()
