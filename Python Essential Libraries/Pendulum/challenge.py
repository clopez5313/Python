import pendulum

# Obtain today's date.
today = pendulum.now()
todayD = today.format("dddd, MMMM Do")
print("Today is:",todayD)

# Get Clash Day.
clashDay = pendulum.datetime(today.year, 2, 7)
clashD = clashDay.format("dddd, MMMM Do")
print("International Clash Day is:",clashD)

# Check if Clash Day already went by.
if clashDay < today:
    difference = clashDay.diff(today)
    dayDifference = difference.in_days()
    print("International Clash Day went by",dayDifference,"days ago")
    clashDay = clashDay.add(years=1)

# Print how many days until next Clash Day.
difference = today.diff(clashDay)
dayDifference = difference.in_days()
print("It's",dayDifference,"days until International Clash Day!")
