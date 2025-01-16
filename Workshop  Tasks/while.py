"""
Set program to always ask for input
declare variable for user input
declare variable for calculation of average
end loop if user inputs -1
calculate and print calculated average

"""
total = 0
no_of_inputs = 0
while True:
    num = int(input("Please enter a number: "))
    if num == -1:
        break
    else:
        total += num
        no_of_inputs += 1
        continue
average = total / no_of_inputs

print(f"The total of the numbers is: {average}")
