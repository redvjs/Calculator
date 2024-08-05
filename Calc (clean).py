import math

# Returns the addition of x, y      
def addition(x, y):
    return x + y
# Returns the subtraction of x, y  
def subtraction(x,y):
    return x - y
# Returns the multiplication of x, y  
def multiplication(x,y):
    return x * y
# Returns the division of x, y  
def division(x,y):
    # Attempts to divide x by y, will catch ZeroDivisionError if denominator is 0.
    try:
        return float(x / y)
    except ZeroDivisionError:
        print("Cant divide by 0. Please try that again!")

# returns the modulus of x,y
def modulus(x,y):
    return x % y

# returns x to the power of y
def power (x,y):
    return x ** y

# returns the factorial of y
def factorial(y):
    return math.factorial(y)

# gets user input as a floating point value. Checks if values inputted are numerical.
def get_int():
    while True:
        try:
            # checks to see if factorial operator is used, in which case only one int is used.
            if operator == "!":
                num_1 = int(input("Number: "))
                return num_1
            # else it will request two integers from the user.
            elif operator == "plot":
                print("Please enter your first list of numbers in the format: 5,4,3,2,1")
                print("You will need to enter first the x-axis list, and then the y-axis list")
                try:
                    x_axis = [input("Enter your first set of numbers (x-axis): ")]
                    y_axis = [input("Enter your second set of numbers (y-axis): ")]
                    return x_axis, y_axis
                except:
                    print("oops")

            else:
                num_1 = int(input("First number: "))
                num_2 = int(input("Second number: "))
                return num_1, num_2
        except ValueError:
            print("You must enter a numeric value")
            pass

# Gets the mathematical operator from the user.
def operation():
    # run whilst loop to check operator input.
    while True:
        operator = input("Please enter an operator (+, -, *, /, %, ^, !, plot): ")
        if operator in ("+, -, *, /, %, ^, !"):
            return operator
        elif operator in ("plot"):
            return operator
        else:
            print("Please make sure you use on of the available operators! ")

# Performs calculation based on operator selected.
def calculation():
    if operator == "+":
        result = float(addition(x,y))
        return result
    if operator == "-":
        result = float(subtraction(x,y))
        return result
    if operator == "*":
        result = float(multiplication(x,y))
        return result
    if operator == "/":
        result = division(x,y)
        return result
    if operator == "%":
        result = float(modulus(x,y))
        return result
    if operator == "^":
        result = float(power(x,y))
        return result
    if operator == "!":
        result = float(factorial(y))
        return result
    if operator == "plot":
        graph()
        return
    
# Runs code through a while loop, initializing variables and printing result of user calculations.
# Checks if program should continue.
while(True):
    operator = operation()
    if operator == "plot":
        x_axis, y_axis = get_int()
        plt.show()
        break
    # checks if factorial is in operation, in which case we only attempt to retrieve one int.
    if operator == "!":
        y = get_int()
    # else, retrieve two ints.
    else:
        x, y = get_int()
    result = calculation()
    if result != None and operator == "!":
        print(f"{y}{operator} = {result:.2f} ")
        # check to see if user wishes to perform another operation.
        carry_on_operation = input("Do you wish to perform another operation?(y/n): ")
        # if user inputs "n", break while loop.
        if carry_on_operation == "n":
            break
    # if not operator == "!", print using x and y + result.
    elif result != None:
        print(f"{x} {operator} {y} = {result:.2f} ")
        # check to see if user wishes to perform another operation.
        carry_on_operation = input("Do you wish to perform another operation?(y/n): ")
        if carry_on_operation == "n":
            break

      
