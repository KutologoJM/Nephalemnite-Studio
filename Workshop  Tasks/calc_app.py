def multiplication():
    """Multiplies two numbers provided by the user,
     creates a string in the format x * y = z and then returns this string."""
    result_multiply = num1 * num2
    result_multiply_str = f"{num1} x {num2} = {result_multiply}"
    print(result_multiply_str)
    return result_multiply_str


def addition():
    """adds two numbers provided by the user,
         creates a string in the format x + y = z and then returns this string."""
    result_add = num1 + num2
    result_add_str = f"{num1} + {num2} = {result_add}"
    print(result_add_str)
    return result_add_str


def subtraction():
    """Subtracts two numbers provided by the user,
         creates a string in the format x - y = z and then returns this string."""
    result_sub = num1 - num2
    result_sub_str = f"{num1} - {num2} = {result_sub}"
    print(result_sub_str)
    return result_sub_str


def division():
    """Divides two numbers provided by the user,
         creates a string in the format x / y = z and then returns this string."""
    result_div = num1 / num2
    result_div_str = f"{num1} / {num2} = {result_div}"
    print(result_div_str)
    return result_div_str


print("Welcome to calc_app.py")  # welcomes user to calc_app.py
while True:
    # function refers to what choice of the 3 provided the user chooses
    function = input("""
1. Calculator
2. Print results
3. Exit program
=> """)
    if function == "1":
        while True:
            # allows user to continuously make calculations or return to 'main menu'
            submenu_option = input("Press 'Enter' to 'continue' or 'menu' to return to main menu\n").lower()
            if submenu_option == "":
                # takes in the two user inputs required for calculator functions
                try:
                    num1 = int(input("Enter first number: "))
                    num2 = int(input("Enter second number: "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                while True:
                    operation = input("Please enter an operation (+, -, *, or /): ")
                    if operation in ["+", "-", "*", "/"]:
                        break
                    else:
                        print("Please enter a valid operation.")
                        continue
                # depending on operator chosen the corresponding function is called taking num1 and num2 as inputs
                # after the function runs, the full equation in the form x + y = z is appended to equations.txt
                if operation == "*":
                    output = multiplication()
                    with open("equations.txt", "a") as file:
                        file.write(f"\n{output}")
                    continue
                elif operation == "+":
                    output = addition()
                    with open("equations.txt", "a") as file:
                        file.write(f"\n{output}")
                    continue
                elif operation == "/":
                    try:
                        output = division()
                    except ZeroDivisionError:
                        print("Cannot divide by zero")
                        output = "Cannot divide by zero"
                        with open("equations.txt", "a") as file:
                            file.write(f"\n{output}")
                    continue
                elif operation == "-":
                    output = subtraction()
                    with open("equations.txt", "a") as file:
                        file.write(f"\n{output}")
                    continue
                break
            elif submenu_option == "menu":  # allows user to return to 'main menu'
                break
            else:
                print("Invalid option selected. Please try again.")
                continue
    elif function == "2":
        try:
            # prints all equations from equations,txt to console
            # if equations.txt does not exist error message is shown to user
            file = open('equations.txt', 'r')
            content = file.read()
            print(content)
            file.close()
        except FileNotFoundError:
            print("There are no contents in equations.txt to view")

        continue
    elif function == "3":  # exits program
        break
    else:
        print("Invalid option")
        continue
