from tkinter import *
import os.path

class Program:

    def __init__(self):
        self.title = "Interfaces with Tkinter!"
        self.icon = os.path.abspath("./images/icon.ico")
        self.icon_alt = os.path.abspath("./Tkinter/images/icon.ico")
        self.size = "720x450"
        self.resizable = False

    def load(self):

        # Root window
        window = Tk()
        self.window = window

        # Check if a file exist
        icon_path = self.icon

        if not os.path.isfile(icon_path):
            icon_path = self.icon_alt

        # Show text
        text = Label(window, text=icon_path)
        text.pack()

        # Window icon
        window.iconbitmap(icon_path)

        # Window title
        window.title(self.title)

        # Change window size
        window.geometry(self.size)

        # Block window size
        if self.resizable:
            window.resizable(1, 1)
        else:
            window.resizable(0, 0)

    def addText(self, text):
        text = Label(self.window, text=text)
        text.pack()

    def showWindow(self):
        # Show window
        self.window.mainloop()


program = Program()
program.load()
program.addText("Hello World")
program.addText("Hello Tkinter")
program.showWindow()
