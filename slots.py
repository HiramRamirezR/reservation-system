from pprint import pprint as pp

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
hours = ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]

slots = {}

for day in days:
    slots[day] = {}
    for hour in hours:
        slots[day][hour] = None