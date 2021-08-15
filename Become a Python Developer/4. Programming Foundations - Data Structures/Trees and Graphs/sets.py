# Create a set.
days = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
months = {"Jan","Feb","Mar"}
dates = {21,22,17}

print(days)
print(months)
print(dates)

# Iterate through the set.
for day in days:
    print(day)

# Add an element to the set.
months.add("Apr")
print(months)

# Remove an element from the set.
dates.discard(22)
print(dates)

# Union of two sets.
otherMonths = {"May","Jun","Jul","Aug"}
combinedMonths = months | otherMonths
print(combinedMonths)

# Intersection of two sets.
otherDates = {17,20,8,28}
combinedDates = dates & otherDates
print(combinedDates)

# Difference of two sets.
combinedDates2 = dates - otherDates
print(combinedDates2)

# Comparison of sets.
allDates = {8,17,20,21,22,28}
subset = dates <= allDates
superset = allDates >= otherDates
print(subset)
print(superset)

# Update a set.
combinedMonths.update(["Sep","Oct","Nov","Dec"])
print(combinedMonths)

# Symmetric difference of two sets.
setA = {1,2,3,4,5,6}
setB = {1,2,9,8,10}
setC = setA ^ setB
print(setC)
