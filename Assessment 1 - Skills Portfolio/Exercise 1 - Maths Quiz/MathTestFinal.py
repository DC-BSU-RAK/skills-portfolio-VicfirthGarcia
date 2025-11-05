from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Math Quiz")
root.geometry("600x600")

title_label = Label(
    root,
    text="MATH QUIZ",
    font=("Arial", 25, "bold"),
    bg="#f5f5f5",
    fg="#333"
)
title_label.pack(pady=40)

#Difficulty Buttons

button1= Button(root, text="Easy", fg="black", bg="green", font=("Arial", 12), width=10, height=2)
button1.pack(pady=5)

button2= Button(root, text="Moderate", fg="black", bg="yellow", font=("Arial", 12), width=10, height=2)
button2.pack(pady=5)

button3= Button(root, text="Advanced", fg="black", bg="red", font=("Arial", 12), width=10, height=2)
button3.pack(pady=5)

root.mainloop()