import json
import tkinter as tk
from tkinter import ttk

# class FormApp(tk.Frame):
#     def __init__(self):
#         super().__init__()
#         self.text = tk.StringVar("Form")


# TODO: Create StringVar for name
# TODO: Create StringVar for name

import tkinter
root = tkinter.Tk()

name_frame = tkinter.Frame(root)
name_frame.pack()
name_label = tkinter.Label(name_frame, text="Name")
name_label.pack(side="left")

name_entry = tkinter.Entry(name_frame)
name_entry.pack(side="right")

# TODO: Create StringVar for age
# TODO: Create StringVar for age

age_frame = tkinter.Frame(root)
age_frame.pack()
age_label = tkinter.Label(age_frame, text="Age")
age_label.pack(side="left")

age_entry = tkinter.Entry(age_frame)
age_entry.pack(side="right")


# TODO: Create StringVar for theme
# TODO: Create StringVar for theme

Theme_frame = tkinter.Frame(root)
Theme_frame.pack()
Theme_label = tkinter.Label(Theme_frame, text="Preferred Theme")
Theme_label.pack(side="left")

# label = tkinter.Label(root, textvariable=Theme_frame)
# Theme_frame.pack(side="left")
# label.pack()

radio_value = tkinter.StringVar()
theme_radio1 = tkinter.Radiobutton(
    Theme_frame, text="Light", variable = Theme_frame, value="Light")
theme_radio1.pack(side="right")

theme_radio2 = tkinter.Radiobutton(
    Theme_frame, text="Dark", variable = Theme_frame, value="Dark"
)
theme_radio2.pack(side="left")


# TODO: Create BooleanVar for subscribe
# TODO: Create BooleanVar for subscribe

check_value = tkinter.BooleanVar()
checkbox = tkinter.Checkbutton(
root,
text="Subscribe to newsletter",
variable = check_value,
)
checkbox.pack()


# TODO: Create IntVar for rating
# TODO: Create IntVar for rating
slider_value = tkinter.IntVar(value= "")
slider = tkinter.Scale(
 root,
from_=0,
to=100,
 orient="horizontal",
 variable=slider_value
 )
slider.pack()
# TODO: Create function for saving values to JSON
# TODO: Create button for submit + save

button = tkinter.Button(root, text="Submit", command="show_input")
button.pack()

# root.bind("<Return>", show_input)
# root.bind("<space>", show_input)
# button = tkinter.Button(root, text="Submit", command=show_input)
# button.pack()
root.mainloop()
