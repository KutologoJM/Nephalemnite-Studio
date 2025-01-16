"""
Replace.py

save given sentence as a string
use replace function to replace ! with a blank space
use upper function to reprint sentence
print sentence in reverse
"""

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

sentence = sentence.replace("!", " ")
print(sentence)
print(sentence.upper())
print(sentence[-1:: -1])
