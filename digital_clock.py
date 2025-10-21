# -------------------------------
# Project: Digital Clock using Python

# Description: A simple real-time digital clock using Tkinter GUI

from tkinter import *
import time


root = Tk()
root.title("Digital Clock by Haritha")  
root.geometry("500x200")  
root.resizable(False, False)  
root.config(bg="black")  


def update_time():
    """This function updates the label with the current time every second."""
    current_time = time.strftime("%I:%M:%S %p")  
    clock_label.config(text=current_time)  
    clock_label.after(1000, update_time) 


clock_label = Label(
    root,
    text="",
    font=("Helvetica", 48, "bold"),  
    fg="#00FFFF",  
    bg="black"  
)
clock_label.pack(pady=40)

title_label = Label(
    root,
    text="DIGITAL CLOCK",
    font=("Arial", 18, "bold"),
    fg="#FFD700",
    bg="black"
)
title_label.pack()

# -------------------------------
# Start the clock
# -------------------------------
update_time()  # Initial call
root.mainloop()  # Keeps the window running
