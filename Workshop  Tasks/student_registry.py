"""
Student Registry code
takes in a number of students that need to register
adds their student id to the list
add a dotted line for each student to be able to sign on

"""

number_of_students = int(input("How many students will be registering today?\n"))
with open('reg_form.txt', 'w') as f:
    f.write("Attendance Registry\n")
    # asks for a new student ID depending on number of participating students entered
    for num in range(number_of_students):
        student_id = input("Enter Student ID:\n")
        # dotted line after each student ID for student to sign on
        f.write(f"{student_id} ................\n")

f.close()
