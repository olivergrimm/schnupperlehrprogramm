def zellers_congruence(day, month, year):
    if month in (1, 2):
        month += 12
        year -= 1

    k = year % 100
    j = year // 100

    h = (day + 13 * (month + 1) // 5 + k + k // 4 + j // 4 - 2 * j) % 7

    days_of_week = ["Samstag", "Sonntag", "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]
    
    return days_of_week[h]


day = 25
month = 12
year = 3000

print(zellers_congruence(day, month, year))

statistik = {
    "Montag": 0,
    "Dienstag": 0,
    "Mittwoch": 0,
    "Donnerstag": 0,
    "Freitag": 0,
    "Samstag": 0,
    "Sonntag": 0
}

startyear = 2023
while startyear <= 3000:
    weekday = zellers_congruence(day, month, startyear)
    
    statistik[weekday] = statistik[weekday]+1
    
    #print(f"Weihnachten ({day}/{month}/{startyear}) wird an einem {weekday} sein.")
    startyear += 1
    
print(statistik)