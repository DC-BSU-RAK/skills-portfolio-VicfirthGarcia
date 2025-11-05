from tkinter import *
from tkinter import ttk
import random

#Main Menu Where You Choose Your Difficulty

def displayMenu():
    title_label.pack(pady=40)
    button1.pack(pady=5)
    button2.pack(pady=5)
    button3.pack(pady=5)

#Random Intergers Based On Difficulty Chosen

def randomInt(difficulty):
    if difficulty == "Easy":
        return random.randint(1, 10), random.randint(1, 10)
    elif difficulty == "Moderate":
        return random.randint(10, 50), random.randint(10, 50)
    elif difficulty == "Advanced":
        return random.randint(50, 100), random.randint(50, 100)

#How The Quiz Funtion Flows

def startQuiz(difficulty):
    global current_difficulty, score, question_count
    current_difficulty = difficulty
    score = 0
    question_count = 0

    # Hiding The Menu

    title_label.pack_forget()
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    result_label.pack_forget()

    displayProblem()

#Displays The Math Question

def displayProblem():
    global num1, num2, operation, correct_answer, question_label, answer_entry, submit_btn

    num1, num2 = randomInt(current_difficulty)
    operation = decideOperation()
    
    if operation == "+":
        correct_answer = num1 + num2
    else:
        correct_answer = num1 - num2
    
    question_label.config(text=f"{num1} {operation} {num2} = ?")
    answer_entry.delete(0, END)
    question_label.pack(pady=20)
    answer_entry.pack()
    submit_btn.pack(pady=10)

#Makes The Quiz Randomly Choose Between Addition, Subtraction, And Multiplication

def decideOperation():
    return random.choice(["+", "-", "*"])

#Answer Submission And Moves To Next Question

def submitAnswer():
    global score, question_count

    user_ans = answer_entry.get()
    if isCorrect(user_ans, correct_answer):
        score += 1
    
    question_count += 1
    if question_count < 10:  # 10 questions per quiz
        displayProblem()
    else:
        displayResults()

#Checks If The User Inputs The Correct Answer

def isCorrect(user_answer, correct_answer):
    try:
        return int(user_answer) == correct_answer
    except:
        return False
    
#Makes The Player Play Again And Choose A Difficulty After Finishing The Quiz
    
def displayMenuAfterQuiz():
    result_label.pack_forget()
    play_again_btn.pack_forget()

    title_label.pack(pady=40)
    button1.pack(pady=5)
    button2.pack(pady=5)
    button3.pack(pady=5)

#Displays Your Results (Score)

def displayResults():
    question_label.pack_forget()
    answer_entry.pack_forget()
    submit_btn.pack_forget()

    final_score = int((score/10) * 100)

    if final_score >= 90:
        grade = "A+"
    elif final_score >= 80:
        grade = "A"
    elif final_score >= 70:
        grade = "B"
    elif final_score >= 60:
        grade = "C"
    else:
        grade = "F"

    result_label.config(text=f"Your Score: {final_score}/100\n  Grade: {grade}")
    result_label.pack(pady=40)
    play_again_btn.pack(pady=20)

root = Tk()
root.title("Math Quiz")
root.geometry("600x600")

#Title Menu

title_label = Label(root, text="MATH QUIZ", font=("Arial", 25, "bold"), bg="#f5f5f5", fg="#333")
title_label.pack(pady=40)

#Difficulty Buttons

button1= Button(root, text="Easy", fg="black", bg="green", font=("Arial", 12), width=10, height=2, command=lambda: startQuiz("Easy"))
button1.pack(pady=5)

button2= Button(root, text="Moderate", fg="black", bg="yellow", font=("Arial", 12), width=10, height=2, command=lambda: startQuiz("Moderate"))
button2.pack(pady=5)

button3= Button(root, text="Advanced", fg="black", bg="red", font=("Arial", 12), width=10, height=2, command=lambda: startQuiz("Advanced"))
button3.pack(pady=5)

question_label = Label(root, text="", font=("Arial", 20), bg="#f5f5f5")
answer_entry = Entry(root, font=("Arial", 16))
submit_btn = Button(root, text="Submit", font=("Arial", 12), command=submitAnswer)
play_again_btn = Button(root, text="Play Again", font=("Arial", 12), command=lambda: displayMenuAfterQuiz())

result_label = Label(root, text="", font=("Arial", 20), bg="#f5f5f5")

root.mainloop()