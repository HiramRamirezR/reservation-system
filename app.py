import os
import json

from slots import days
from slots import week


complete = None

while complete == None:

    print("Welcome to the Reservation System!\n")
    print("Choose an option")
    print("""
    1. View available slots
    2. Create reservation
    3. View current reservations
    4. Cancel reservation
    5. Exit
    """)

    option = int(input(">> "))

    if option == 1:
        print("\nAvailable slots:\n")

        slots_in_day = []
        for day in week:
            print(f">> {day}")
            for slot in week[day]:
                if week[day][slot] == None:
                    slots_in_day.append(slot)
            print(f"{slots_in_day}\n")
            slots_in_day = []

    elif option == 2:
        name = input("\nEnter your name:\n\n>> ")
        print("\nSelect day:\n")
        for day in enumerate(week):
            print(f"{day[0] + 1}. {day[1]}")

        selected_day_index = int(input("\n>> ")) - 1
        selected_day = days[selected_day_index]
        print(f"\nSelected day: {selected_day}")
        print("\nSelect a slot:\n")

        available_slots = []
        for slot, v in week[selected_day].items():
            if v == None:
                available_slots.append(slot)

        for i in enumerate(available_slots):
            print(f"{i[0] + 1}. {i[1]}")

        slot = int(input("\n>> ")) - 1
        slot_selected = available_slots[slot]

        print(f"\nReservation for: {name} - On {selected_day} at {slot_selected}")
        print("\nConfirm reservation?")
        confirm_reservation = input("\ny/n:\n>> ")

        while True:
            if confirm_reservation.lower() == "y":
                week[selected_day][slot_selected] = name
                print("\nReservation confirmed!")
                break
            elif confirm_reservation == "n":
                print("\nReservation cancelled!")
                break
            else:
                print("\nInvalid option. Please select 'y' or 'n'.")



