days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
hours = ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]

week = {}

for day in days:
    week[day] = {}
    for hour in hours:
        week[day][hour] = None