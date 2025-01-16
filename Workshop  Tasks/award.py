"""
Determines what award a competitor earned
Input the times (in minutes) for each event
calculate the total time
display total time along with award earned

"""

print("Please enter your official time for each event in minutes.")
swimming_time = int(input("Swimming event: "))
cycling_time = int(input("Cycling event: "))
running_time = int(input("Running event: "))

total_time = swimming_time + cycling_time + running_time

print(f"The participant took a combined time of {total_time} minutes to complete the Triathlon.")
if total_time <= 100:
    print("The contestant has been awarded Provincial Colours for their participation.")
elif total_time > 100 and total_time <= 105:
    print("The contestant has been awarded Provincial Half Colours for their participation.")
elif total_time > 105 and total_time <= 110:
    print("The contestant has been awarded a Provincial Scroll for their participation.")
else:
    print("No reward has been awarded to the participant.")
