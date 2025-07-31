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
    print("Available slots:")
    print(slots)

# Enter your name: Hiram
# Select slot:
# 1. Monday 9:00–10:00
# 2. Monday 10:00–11:00
# >> 1

# ✅ Reservation confirmed for Hiram on Monday 9:00–10:00
