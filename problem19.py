#1 Jan 1901 to 31 Dec 2000
#sundays in January from

firstNormal = { 1, 32, 60, 91, 121, 152, 182, 213, 244,274, 305, 335}
firstLeap = { 1, 32, 61, 92, 122, 153, 183, 213, 245, 275, 306, 335}
dayOfWeek = 2
startYear = 1901
sundays = 0

for year in range(1901, 2001):
    if year % 4 == 0:
        days = 367
        first = firstLeap
    else :
        first = firstNormal
        days = 366
    for day in range(1, days):
        #if dayOfWeek % 7 == 0:
        if dayOfWeek % 7 == 0 and day in first :
            sundays += 1
        dayOfWeek += 1

print (sundays)

