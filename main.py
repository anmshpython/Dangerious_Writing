import tkinter.messagebox
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
THEME_COLOR = "#375362"
initial_time_value = 5
time_count = initial_time_value
timer = None


# ---------------------------- FUNCTIONS ------------------------------- #
def my_callback(var, index, mode):
    timer_reset()
    global time_count
    # if len(a_var.get()) > 0:
    time_count = initial_time_value
    start_timer()


def timer_reset():
    window.after_cancel(timer)


def start_timer():
    global time_count
    if time_count > 0:
        global timer
        timer = window.after(1000, start_timer)
        time_count -= 1
    else:
        massage = typing_text.get()
        typing_text.delete(0, END)
        tkinter.messagebox.showinfo("Here is your typed text", f"{massage}")


# ---------------------------- UI ------------------------------- #
window = Tk()
window.title("Dangerous Writing")
window.config(width=600, height=800, padx=20, pady=20, bg=THEME_COLOR)

# Set the variable
a_var = StringVar()
a_var.trace_add("write", my_callback)

# Type entry text
typing_text = Entry(font=("Arial", 20), width=60, highlightthickness=0, highlightbackground="white", textvariable=a_var)
typing_text.focus_set()
typing_text.grid(row=2, column=0, columnspan=3, pady=20)

start_timer()

window.mainloop()
