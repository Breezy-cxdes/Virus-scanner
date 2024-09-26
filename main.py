from tkinter import *
from tkinter import messagebox

# Setup Tkinter Window
root = Tk()
root.geometry("200x200")

# Function for Displaying Warning Message
def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found.")

# Adding Button Widget to Window
button = Button(root, text="Scan for Virus", command=msg)  # Correct button initialization
button.place(x=40, y=80)

# Entering main event loop
root.mainloop()
