import os

# Create a 2D array and print some of their elements.
studentGrades = [[72, 85, 87, 90, 69], [80, 87, 65, 89, 85], [96, 91, 70, 78, 97], [90, 93, 91, 90, 94], [57, 89, 82, 69, 60]]
print(studentGrades[1])
print(studentGrades[0])
print(studentGrades[2])
print(studentGrades[3][4])

# Traverse the array.
for student in studentGrades:
    for grade in student:
        print(grade, end=" ")
    print()

# Insert an element into the 2D array.
os.system("cls")
studentGrades.insert(1, [84, 93, 72, 60, 75])

for student in studentGrades:
    for grade in student:
        print(grade, end=" ")
    print()

# Update elements of the array.
studentGrades[0] = [77, 90, 92, 95, 74]
studentGrades[1][2] = 77
os.system("cls")

for student in studentGrades:
    for grade in student:
        print(grade, end=" ")
    print()

# Delete elements of the array.
del(studentGrades[0][2])
del(studentGrades[1])
os.system("cls")

for student in studentGrades:
    for grade in student:
        print(grade, end=" ")
    print() 
