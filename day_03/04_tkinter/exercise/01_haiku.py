assert True

import tkinter

root = tkinter.Tk()
root.title("Sample GUI Application")
root.geometry("600x400")
label = tkinter.Label(root, text="Enter your password:")
label.pack(side="top")


user_input = tkinter.StringVar(root, value="")
password = tkinter.Entry(root, textvariable=user_input)
password.pack()

text = tkinter.StringVar(root, value="Password")
label = tkinter.Label(root, textvariable=text)
label.pack()

root.geometry("800x400")
def show_input(event = None):
    given_text = user_input.get()
    label.pack()
    print(given_text)
    if given_text == "Mary Ann":
       text.set("Access Granted")

    else:
        text.set("Access Denied")


message = "Input password"

root.bind("<Return>", show_input)
root.bind("<space>", show_input)

button = tkinter.Button(root, text="Submit", command="")
button.pack()
root.mainloop()

# message = """
# Loops within loops spin,
# A silent function returns,
# The logic is clear
# """


# TODO: Show message using a label
#
# label = tkinter.Label(root,
#                       text=message,
#                       font=("Arial", 25, "bold italic"),
#                       fg = "red",
#                       bg = "black"
# )
# label.pack()
# root.mainloop()

