import tkinter as tk

listy = ["GT", "Del", "CE", "ON/C", "7", "8", "9","/", "4", "5", "6", "X", "1", "2", "3", "-", "0", ".","=","+"]
ticker = 0
window = tk.Tk()

for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

for i in range(5):
    for j in range(4):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1,
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=listy[ticker], padx=20,pady=20)
        ticker +=1
        label.pack()

events = []

# Create an event handler
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

# Run the event loop
window.mainloop()

while True:
    if events == []:
        continue

    event = events[0]

    # If event is a keypress event object
    if event.type == "keypress":
        # Call the keypress event handler
        handle_keypress(event)