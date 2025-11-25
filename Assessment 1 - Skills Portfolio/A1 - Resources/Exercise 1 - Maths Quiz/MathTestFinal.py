from tkinter import *
import random

root = Tk()
import tkinter as tk
icon = tk.PhotoImage(file="Assessment 1 - Skills Portfolio\A1 - Resources\Exercise 1 - Maths Quiz\math.png")
root.iconphoto(False, icon)
root.title("Math Quiz")
root.geometry("600x400")
root.configure(bg="lightblue")

#Frames For Each Screen

start_frame = Frame(root, bg="lightblue")
instructions_frame = Frame(root, bg="lightblue")
menu_frame = Frame(root, bg="lightblue")
quiz_frame = Frame(root, bg="lightblue")
result_frame = Frame(root, bg="lightblue")

for frame in (start_frame, instructions_frame, menu_frame, quiz_frame, result_frame):
    frame.place(relwidth=1, relheight=1)

def show_frame(frame):
    frame.tkraise()

#Start Menu Screen

title_label = Label(start_frame, text="MATH QUIZ", font=("Arial", 25, "bold"), bg="lightblue", fg="#333")
title_label.pack(pady=40)

start_btn = Button(start_frame, text="Start Game", font=("Arial", 14), width=12,
                   command=lambda: show_frame(instructions_frame))
start_btn.pack(pady=20)

#Instructions

instructions_label = Label(
    instructions_frame,
    text="Welcome To The Math Quiz!\n\n"
         "You will answer 10 questions in total.\n"
         "Your score and grade will be shown at the end.\n\n"
         "Click 'Continue' to choose a difficulty.",
    font=("Arial", 16),
    bg="lightblue"
)
instructions_label.pack(pady=40)

continue_btn = Button(instructions_frame, text="Continue", font=("Arial", 14),
                      command=lambda: show_frame(menu_frame))
continue_btn.pack(pady=20)

#Difficulties

Label(menu_frame, text="Choose Difficulty", font=("Arial", 25, "bold"), bg="lightblue").pack(pady=40)

button1 = Button(menu_frame, text="Easy", fg="black", bg="green", font=("Arial", 12),
                 width=10, height=2, command=lambda: startQuiz("Easy"))
button1.pack(pady=5)

button2 = Button(menu_frame, text="Moderate", fg="black", bg="yellow", font=("Arial", 12),
                 width=10, height=2, command=lambda: startQuiz("Moderate"))
button2.pack(pady=5)

button3 = Button(menu_frame, text="Advanced", fg="black", bg="red", font=("Arial", 12),
                 width=10, height=2, command=lambda: startQuiz("Advanced"))
button3.pack(pady=5)

#Quiz Screen

question_label = Label(quiz_frame, text="", font=("Arial", 20), bg="lightblue")
question_label.pack(pady=20)

answer_entry = Entry(quiz_frame, font=("Arial", 16))
answer_entry.pack()

feedback_label = Label(quiz_frame, text="", font=("Arial", 14), bg="lightblue")
feedback_label.pack(pady=10)

submit_btn = Button(quiz_frame, text="Submit", font=("Arial", 12))
submit_btn.pack(pady=10)


#How Quiz Works

def randomInt(difficulty):
    if difficulty == "Easy":
        return random.randint(1, 10), random.randint(1, 10)
    elif difficulty == "Moderate":
        return random.randint(10, 50), random.randint(10, 50)
    elif difficulty == "Advanced":
        return random.randint(50, 100), random.randint(50, 100)

def decideOperation():
    return random.choice(["+", "-", "*", "/"])

current_question = 0
attempts_left = 3

def startQuiz(difficulty):
    global current_difficulty, score, current_question, attempts_left

    current_difficulty = difficulty
    score = 0
    current_question = 0
    attempts_left = 3

    show_frame(quiz_frame)
    displayProblem()

def displayProblem():
    global num1, num2, operation, correct_answer, attempts_left, current_question

    attempts_left = 3

    num1, num2 = randomInt(current_difficulty)
    operation = decideOperation()

    if operation == "+":
        correct_answer = num1 + num2
    elif operation == "-":
        correct_answer = num1 - num2
    elif operation == "*":
        correct_answer = num1 * num2
    else:
        correct_answer = round(num1 / num2, 2)

    question_label.config(text=f"Question {current_question + 1}/10:\n{num1} {operation} {num2} = ?")
    answer_entry.delete(0, END)
    feedback_label.config(text="")

def submitAnswer():
    global score, current_question, attempts_left

    user_input = answer_entry.get()

    try:
        user_answer = float(user_input)
    except:
        feedback_label.config(text="Enter a valid number.")
        return

    #Correct Answer
    if user_answer == correct_answer:
        score += 1
        feedback_label.config(text="Correct!")

        root.after(1000, nextQuestion)
        return

    #If You Answer Incorrectly
    attempts_left -= 1

    if attempts_left > 0:
        feedback_label.config(
            text=f"Incorrect! Try again.\nAttempts left: {attempts_left}"
        )
        answer_entry.delete(0, END)
    else:
        feedback_label.config(
            text=f"Incorrect! The correct answer was {correct_answer}."
        )
        root.after(1500, nextQuestion)

submit_btn.config(command=submitAnswer)

def nextQuestion():
    global current_question

    current_question += 1

    if current_question >= 10:
        displayResults()
    else:
        displayProblem()

#Result Screen

result_label = Label(result_frame, text="", font=("Arial", 20), bg="lightblue")
result_label.pack(pady=40)

play_again_btn = Button(result_frame, text="Play Again", font=("Arial", 14),
                        command=lambda: show_frame(menu_frame))
play_again_btn.pack(pady=20)

def displayResults():
    percent = int((score / 10) * 100)

    if percent >= 90:
        grade = "A+"
    elif percent >= 80:
        grade = "A"
    elif percent >= 70:
        grade = "B"
    elif percent >= 60:
        grade = "C"
    else:
        grade = "F"

    result_label.config(text=f"Your Score: {percent}/100\nGrade: {grade}")
    show_frame(result_frame)

show_frame(start_frame)
root.mainloop()
