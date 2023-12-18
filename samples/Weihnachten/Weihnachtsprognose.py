def zellers_congruence(day, month, year):
    if month in (1, 2):
        month += 12
        year -= 1

    k = year % 100
    j = year // 100

    h = (day + 13 * (month + 1) // 5 + k + k // 4 + j // 4 - 2 * j) % 7

    days_of_week = ["Samstag", "Sonntag", "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]
    
    return days_of_week[h]

print("hallo")