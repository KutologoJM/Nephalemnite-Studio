"""
Ask user for 3 integers
get 3 integers
calculate the:
sum of the 3 integers
1st integer minus 2nd integer
3rd integer multiplied by 1st integer
sum of integers divided by 3rd integer

"""

print("Please enter 3 different integers")
integer1 = int(input("First integer: "))
integer2 = int(input("Second integer: "))
integer3 = int(input("Third integer: "))

sum_integers = integer1 + integer2 + integer3
print(f"The sum of the numbers is equal to {sum_integers}.")
print(f"Integer one minus integer two is equal to {integer1 - integer2}.")
print(f"Integer three multiplied by integer one is equal to {integer3 * integer1}.")
print(f"The sum of the numbers divided by integer three is equal to {sum_integers // integer3}.")
