from slots import slots

print("Welcome to the Reservation System!\n")
print("Choose an option")
print("""
1. View available slots
2. Create reservation
3. View current reservations
4. Cancel reservation/n
5. Exit
""")

option = int(input(">> "))

if option == 1:
    print("\nAvailable slots:\n")

    slots_in_day = []
    for day in slots:
        print(f">> {day}")
        for slot in slots[day]:
            if slots[day][slot] == None:
                slots_in_day.append(slot)
        print(f"{slots_in_day}\n")
        slots_in_day = []

elif option == 2:
    name = input("Enter your name: ")
    print("Select day:")
    for day in enumerate(slots):
        print(f"{day[0] + 1}. {day[1]}")

    selected_day = int(input(">> ")) - 1
    print("Select slot:")


# Enter your name: Hiram
# Select slot:
# 1. Monday 9:00–10:00
# 2. Monday 10:00–11:00
# >> 1

# ✅ Reservation confirmed for Hiram on Monday 9:00–10:00
