# Calculator
Simple Python Calculator, and Calculator GUI using tkinter

Calculator Program:

    This is a simple Python calculator program that performs various mathematical operations including addition, subtraction, multiplication, division, modulus, power, factorial. The program interacts with the user to get the required input and displays
    the result of the computation.

Features:

    - Addition
    - Subtraction
    - Multiplication
    - Division
    - Modulus
    - Power
    - Factorial
    - Functions
    - addition(x, y)
    - Returns the sum of x and y.

Future Features:

    - Creating graphs with matplotlib
    - Further operations

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

---------------------------------------------------------------------------------------

Tkinter Calculator Interface
    This Python program creates a simple graphical user interface (GUI) for a calculator using the Tkinter library. It sets up a grid of buttons representing different calculator operations and digits.

Features:

        GUI layout with buttons for digits and basic calculator operations.
        Event handling for key presses.
        Components
        Libraries
        tkinter: For creating the GUI.
        Variables
        listy: List of strings representing button labels.
        ticker: Index to iterate over listy and assign labels to buttons.
        window: Main application window.
Grid Configuration
    The grid is configured to have:
    
        3 columns with equal weight and a minimum size of 75.
        5 rows with equal weight and a minimum size of 50.
        
Creating Buttons:
    Buttons are created in a nested loop:

        The outer loop iterates over the rows.
        The inner loop iterates over the columns.
        Each button is placed inside a frame with raised relief and a border.
        Buttons are labeled with values from the listy list.
        
Event Handling:

    handle_keypress(event): Function to handle keypress events and print the character associated with the key pressed.
    The main loop runs to keep the window active and check for events.
    
Code

import tkinter as tk

# List of button labels
listy = ["GT", "Del", "CE", "ON/C", "7", "8", "9", "/", "4", "5", "6", "X", "1", "2", "3", "-", "0", ".", "=", "+"]
ticker = 0
window = tk.Tk()

# Configure grid columns and rows
for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

# Create buttons in a grid layout
for i in range(5):
    for j in range(4):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1,
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=listy[ticker], padx=20, pady=20)
        ticker += 1
        label.pack()

# Event list
events = []

# Event handler for keypress
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

# Run the event loop
window.mainloop()

# Check for events (not functional within the Tkinter main loop context)
while True:
    if events == []:
        continue

    event = events[0]

    # If event is a keypress event object
    if event.type == "keypress":
        # Call the keypress event handler
        handle_keypress(event)
Usage:

    Run the program.
    The Tkinter window will appear with buttons arranged in a grid.
    Press any key to see the character printed in the console (note that the event handling part for key presses is not fully functional within the Tkinter main loop in this code).
Notes:

    The event handling part in the while True loop after window.mainloop() is not functional as written because the Tkinter main loop already handles events. The event loop and handling should be integrated differently to work within Tkinter's framework.
    For a fully functional calculator, additional logic to handle button clicks and perform calculations would be needed.
