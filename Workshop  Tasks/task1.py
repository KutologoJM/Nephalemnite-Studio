"""
code to output the star pattern
*
**
***
****
*****
****
***
**
*

"""

for i in range(10):
    if i < 5:
        i += 1
        print("*" * i)
    else:
        i = 9 - i
        print("*" * i)
