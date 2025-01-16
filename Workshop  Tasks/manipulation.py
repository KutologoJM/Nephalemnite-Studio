"""
Ask user to enter a sentence
save input in str_manip
display length of sentence given
find and replace every occurrence of the sentence's last letter with @
print the last 3 characters in the sentence backwards
create a 5-letter word using the first 3 and last 2 characters from the sentence


"""

str_manip = input("Please enter a sentence: ")

print(f"Your sentence is {len(str_manip)} characters long.")
print(str_manip.replace(str_manip[-1], "@"))
print(str_manip[-1: -4: -1])
print(str_manip[0: 3] + str_manip[-2:])
