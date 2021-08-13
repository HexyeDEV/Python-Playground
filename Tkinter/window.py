from tkinter import *
import os.path

# Root window
window = Tk()

# Check if a file exist
icon_path = os.path.abspath("./images/icon.ico")

if not os.path.isfile(icon_path):
    icon_path = os.path.abspath("./Tkinter/images/icon.ico")

# Show text
text = Label(window, text=icon_path)
text.pack()

# Window icon
window.iconbitmap(icon_path)

# Window title
window.title("Interfaces with Tkinter!")

# Change window size
window.geometry("750x450")

# Block window size
window.resizable(0, 0)

# Show window
window.mainloop()
