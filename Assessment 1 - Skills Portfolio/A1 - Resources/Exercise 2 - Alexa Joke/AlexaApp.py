import tkinter as tk
from tkinter import PhotoImage
import random
import winsound #For Laugh SFX

def get_jokes(filename):
    jokes = []
    with open(filename, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    buffer = []
    for line in lines:
        if line:
            buffer.append(line)
        else:
            if len(buffer) >= 2:
                jokes.append((buffer[0], buffer[1]))
            buffer = []
    if len(buffer) >= 2:
        jokes.append((buffer[0], buffer[1]))

    return jokes


class TheFunny:
    def __init__(self, root):
        self.root = root
        self.root.title("Minion Joke Assistant")
        self.root.config(bg="#FFEB3B")

        self.laugh_sound = r"C:\Users\Vicfirth Garcia\Documents\GitHub\skills-portfolio-VicfirthGarcia\Assessment 1 - Skills Portfolio\A1 - Resources\Exercise 2 - Alexa Joke\minions_laugh.wav"

        try:
            self.minion_img = PhotoImage(file=r"C:\Users\Vicfirth Garcia\Documents\GitHub\skills-portfolio-VicfirthGarcia\Assessment 1 - Skills Portfolio\A1 - Resources\Exercise 2 - Alexa Joke\minion.png"
        )
            img_label = tk.Label(root, image=self.minion_img, bg="#FFEB3B")
            img_label.pack(pady=10)
        except:
            pass

        self.jokes = get_jokes(
            r"C:\Users\Vicfirth Garcia\Documents\GitHub\skills-portfolio-VicfirthGarcia\Assessment 1 - Skills Portfolio\A1 - Resources\Exercise 2 - Alexa Joke\randomJokes.txt"
        )
        self.current_joke = None

        self.setup_label = tk.Label(
            root,
            text="",
            font=("Comic Sans MS", 16, "bold"),
            wraplength=450,
            bg="#FFEB3B",
            fg="#1A237E",
        )
        self.setup_label.pack(pady=10)

        self.punchline_label = tk.Label(
            root,
            text="",
            font=("Comic Sans MS", 14),
            wraplength=450,
            bg="#FFEB3B",
            fg="#0D47A1",
        )
        self.punchline_label.pack(pady=5)
        button_style = {
            "font": ("Comic Sans MS", 12, "bold"),
            "bg": "#1976D2",
            "fg": "white",
            "activebackground": "#0D47A1",
            "activeforeground": "white",
            "padx": 20,
            "pady": 10,
            "bd": 0,
            "relief": "flat"
        }

        tk.Button(root, text="Tell Me a Joke", command=self.show_setup, **button_style).pack(pady=8)
        tk.Button(root, text="Show Punchline", command=self.show_punchline, **button_style).pack(pady=8)
        tk.Button(root, text="Next Joke", command=self.show_setup, **button_style).pack(pady=8)
        tk.Button(root, text="Quit", command=root.quit, **button_style).pack(pady=8)

    def show_setup(self):
        self.current_joke = random.choice(self.jokes)
        setup, _ = self.current_joke

        self.setup_label.config(text=setup)
        self.punchline_label.config(text="")

    def show_punchline(self):
        if self.current_joke:
            _, punchline = self.current_joke
            self.punchline_label.config(text=punchline)
            winsound.PlaySound(self.laugh_sound, winsound.SND_FILENAME | winsound.SND_ASYNC)


root = tk.Tk()
app = TheFunny(root)
root.mainloop()

