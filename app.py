from slots import days
from slots import week

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
    print(f"\nSlot selected: {slot_selected}")
    print("\nConfirm reservation?\n")

    print(f"Reservation: {name} - {selected_day} at {slot_selected}\n")
    confirm_reservation = input("y/n:\n>> ")

    if confirm_reservation == "y":
        print("Reservation confirmed!")
    else:
        print("Reservation cancelled!")


