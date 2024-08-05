# Calculator
Simple Python Calculator, and Calculator GUI using tkinter

Calculator Program:

    This is a simple Python calculator program that performs various mathematical operations including addition, subtraction, multiplication, division, modulus, power, factorial. The program interacts with the user to get the required input and displays
    the result of the computation.

Features:

    Addition
    Subtraction
    Multiplication
    Division
    Modulus
    Power
    Factorial
    Functions
    addition(x, y)
    Returns the sum of x and y.

  subtraction(x, y):
  
    Returns the difference when y is subtracted from x.

  multiplication(x, y):
    
    Returns the product of x and y.

  division(x, y):
  
    Returns the result of dividing x by y. If y is 0, it catches the ZeroDivisionError and prompts the user to try again.

  modulus(x, y):
  
    Returns the remainder when x is divided by y.

  power(x, y):
    
    Returns x raised to the power of y.
  
  factorial(y):
  
    Returns the factorial of y.

  get_int():
  
    Gets user input as integers. It checks if the values inputted are numerical and handles different cases based on the operator:

For factorial (!), it requests a single integer.
For other operations, it requests two integers.

  operation():
  
    Gets the mathematical operator from the user. Ensures that the operator is valid.

  calculation():
  
    Performs the calculation based on the operator selected. Calls the appropriate function and returns the result.

Main Program Loop:

  The main part of the program runs in a while loop:

    Gets the operator from the user.
    Retrieves the required numbers based on the operator.
    Performs the calculation.
    Displays the result.
    Asks the user if they wish to perform another operation. If not, it exits the loop.

Usage:

    Run the program.
    Input the desired operation (+, -, *, /, %, ^, !, plot).
    Enter the numbers when prompted.
    View the result.
    Choose to continue with another operation or exit.
  
Notes:

    For division, if the user attempts to divide by 0, the program will catch the error and prompt the user to enter a valid denominator.
    For factorial, the program requests only one integer.
  
Example:

    Please enter an operator (+, -, *, /, %, ^, !, plot): +
    First number: 10
    Second number: 5
    10 + 5 = 15.00 
    Do you wish to perform another operation?(y/n): n
    
Dependencies
math library for factorial calculation.
Ensure you have the necessary libraries installed before running the program.
