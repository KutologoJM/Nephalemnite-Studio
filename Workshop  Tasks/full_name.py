"""
Ask user to input their full name
Check to see if name is:
Not blank
is more than 4 characters
less than 25 characters
If name meets requirements print thank you message
Otherwise print provided error messages

"""

full_name = input("Please enter your full name: ")

if len(full_name) == 0:
    print("You haven’t entered anything. Please enter your full name.")
elif len(full_name) < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
elif len(full_name) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
else:
    print("Thank you for entering your name.")
