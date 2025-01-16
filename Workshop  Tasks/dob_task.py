"""
Read data from provided DOB.txt and print out in two segments the names and birthdate

"""
# stores information from txt file inside variable named information
file = open("DOB.txt", "r+")
information = ""

for line in file:
    information = information + line
file.close()


names = []
birthdates = []

# separates each person and their date of birth to a new line
information = information.split("\n")

"""
for each of the 25 entries in information:
separate name and birthdate
append names to list "names"
append birthdate to list "birthdates"
"""

i = 0
while i < 25:
    string = information[i]
    string = string.split()
    names.append(f"{string[0]} {string[1]}")
    birthdates.append(f"{string[2]} {string[3]} {string[4]}")
    i += 1

print("Name")
for i in range(len(names)):
    print(names[i])
print("\nBirthdate")
for i in range(len(birthdates)):
    print(birthdates[i])

