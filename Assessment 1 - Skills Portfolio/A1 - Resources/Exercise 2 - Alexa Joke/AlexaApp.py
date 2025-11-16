import tkinter as tk
import random

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
        self.root.title("Joke Assistant")

        self.jokes = get_jokes(r"C:\Users\Vicfirth Garcia\Documents\GitHub\skills-portfolio-VicfirthGarcia\Assessment 1 - Skills Portfolio\A1 - Resources\Exercise 2 - Alexa Joke\randomJokes.txt")
        self.current_joke = None

        # Labels
        self.setup_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400)
        self.setup_label.pack(pady=10)

        self.punchline_label = tk.Label(root, text="", font=("Arial", 12), fg="blue", wraplength=400)
        self.punchline_label.pack(pady=5)

        # Buttons
        tk.Button(root, text="Alexa, tell me a Joke", command=self.show_setup).pack(pady=5)
        tk.Button(root, text="Show Punchline", command=self.show_punchline).pack(pady=5)
        tk.Button(root, text="Next Joke", command=self.show_setup).pack(pady=5)
        tk.Button(root, text="Quit", command=root.quit).pack(pady=5)

    def show_setup(self):
        self.current_joke = random.choice(self.jokes)
        setup, _ = self.current_joke

        self.setup_label.config(text=setup)
        self.punchline_label.config(text="")


    def show_punchline(self):
        if self.current_joke:
            _, punchline = self.current_joke
            self.punchline_label.config(text=punchline)

root = tk.Tk()
app = TheFunny(root)
root.mainloop()
