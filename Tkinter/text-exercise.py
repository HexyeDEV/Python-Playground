from tkinter import *


def test(name, surname, country):
    return f"Hi {name} {surname} i see you are from {country}"


window = Tk()
window.geometry("700x500")

text = Label(window, text=test(surname="Gonzalez", name="Alan", country="Mexico"))
text.config(
    fg="white",
    bg="#000000",
    padx=50,
    pady=20,
    font=("Consolas", 12),
    justify=RIGHT
)
text.pack()

text = Label(window, text="I'm Alan")
text.config(
    height=3,
    bg="orange",
    font=("Arial", 18),
    cursor="circle"
)
text.pack(anchor=SE)

window.mainloop()
