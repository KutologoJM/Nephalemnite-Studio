"""
Part 1- take in string and convert each alternate "character" to uppercase
and each other to lowercase

Part 2- take in string and convert each alternate "word" to uppercase
and each other to lowercase

Process:
1. Input original string
2. create a blank container string
3. add corresponding letter (upper/lower) to container
"""

# part 1 of task
string = "Hello World!"
i = 0
new_string = ""

while i < len(string):
    if i % 2 == 0:
        new_string += string[i].upper()
        i += 1
    else:
        new_string += string[i].lower()
        i += 1
print(new_string)

# part 2 of task

sentence = "I am learning to code"
new_sentence = sentence.split()

for i in range(len(new_sentence)):
    if i % 2 != 0:
        new_sentence[i] = new_sentence[i].upper()
    else:
        new_sentence[i] = new_sentence[i].lower()

print(" ".join(new_sentence))
