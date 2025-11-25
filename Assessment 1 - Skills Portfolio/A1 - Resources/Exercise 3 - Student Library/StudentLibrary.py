import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from PIL import Image, ImageTk

#Functions

def load_students(filename="Assessment 1 - Skills Portfolio\A1 - Resources\Exercise 3 - Student Library\studentMarks.txt"):
    students = []
    try:
        with open(filename, "r") as f:
            lines = f.read().strip().splitlines()
            count = int(lines[0])
            for line in lines[1:]:
                parts = line.split(",")
                num = int(parts[0])
                name = parts[1]
                c1, c2, c3 = map(int, parts[2:5])
                exam = int(parts[5])
                students.append({"Number": num, "Name": name, "C1": c1, "C2": c2, "C3": c3, "Exam": exam})
    except:
        messagebox.showerror("Error", "Could not load studentMarks.txt")
    return students

def save_students(students, filename="studentMarks.txt"):
    with open(filename, "w") as f:
        f.write(str(len(students)) + "\n")
        for s in students:
            line = f"{s['Number']},{s['Name']},{s['C1']},{s['C2']},{s['C3']},{s['Exam']}\n"
            f.write(line)

def calc_total(s):
    return s["C1"] + s["C2"] + s["C3"] + s["Exam"]

def calc_percentage(s):
    return round(calc_total(s) / 160 * 100, 2)

def calc_grade(p):
    if p >= 70:
        return "A"
    elif p >= 60:
        return "B"
    elif p >= 50:
        return "C"
    elif p >= 40:
        return "D"
    else:
        return "F"

#TKinter App

class StudentManagerApp:
    def __init__(self, root):
        self.root = root
        root.title("Student Manager")
        root.configure(bg="#24273A")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", font=("Segoe UI", 10), padding=8, background="#3a3a50", foreground="white")
        style.map("TButton", background=[("active", "#4a4a60")])
        style.configure("TFrame", background="#24273A")
        main_frame = ttk.Frame(root, padding=10)
        main_frame.grid(row=0, column=0)
        sidebar = ttk.Frame(root, padding=10)
        sidebar.grid(row=0, column=1, sticky="ns")

        self.output = tk.Text(main_frame, width=80, height=30, bg="#3E4255", fg="white", insertbackground="white", font=("Consolas", 10))
        self.output.grid(row=0, column=0, padx=10, pady=10)

        #Buttons

        self.make_button(sidebar, "1. View All Students", self.view_all)
        self.make_button(sidebar, "2. View Individual Student", self.view_individual)
        self.make_button(sidebar, "3. Highest Score", self.highest_score)
        self.make_button(sidebar, "4. Lowest Score", self.lowest_score)
        self.make_button(sidebar, "5. Sort Students", self.sort_students)
        self.make_button(sidebar, "6. Add Student", self.add_student)
        self.make_button(sidebar, "7. Delete Student", self.delete_student)
        self.make_button(sidebar, "8. Update Student", self.update_student)

        logo_img = Image.open("Assessment 1 - Skills Portfolio\A1 - Resources\Exercise 3 - Student Library\BSU.png")
        logo_img = logo_img.resize((200, 50))
        self.logo_photo = ImageTk.PhotoImage(logo_img)

        logo_label = tk.Label(sidebar, image=self.logo_photo, background="#1e1e2f")
        logo_label.pack(pady=20)


        #Load Students

        self.students = load_students()

    def make_button(self, frame, text, cmd):
        ttk.Button(frame, text=text, command=cmd).pack(pady=6, fill="x")

    def clear(self):
        self.output.delete("1.0", tk.END)

    def format_student(self, s):
        total = calc_total(s)
        percent = calc_percentage(s)
        grade = calc_grade(percent)

        return (f"Name: {s['Name']}\n"f"Number: {s['Number']}\n"
                f"Coursework Total: {s['C1'] + s['C2'] + s['C3']}/60\n"
                f"Exam Mark: {s['Exam']}/100\n"
                f"Overall %: {percent}%\n"
                f"Grade: {grade}\n"
                f"════════════════════════════════════\n")

    #For All Students

    def view_all(self):
        self.clear()
        total_percent = 0

        for s in self.students:
            percent = calc_percentage(s)
            total_percent += percent
            self.output.insert(tk.END, self.format_student(s))

        avg = round(total_percent / len(self.students), 2)
        self.output.insert(tk.END, f"\nTotal Students: {len(self.students)}\n")
        self.output.insert(tk.END, f"Average Percentage: {avg}%\n")

    #Individual Students

    def view_individual(self):
        code = simpledialog.askstring("Find Student", "Enter Student Number Or Name (First Or Last):")

        if not code:
            return

        matches = [s for s in self.students if code.lower() in s["Name"].lower() or code == str(s["Number"])]

        self.clear()

        if not matches:
            self.output.insert(tk.END, "No Student Found.")
            return

        for s in matches:
            self.output.insert(tk.END, self.format_student(s))

    #For Highest Score

    def highest_score(self):
        if not self.students:
            return
        best = max(self.students, key=lambda s: calc_total(s))
        self.clear()
        self.output.insert(tk.END, "Highest Score:\n\n")
        self.output.insert(tk.END, self.format_student(best))

    #For Lowest Score

    def lowest_score(self):
        if not self.students:
            return
        worst = min(self.students, key=lambda s: calc_total(s))
        self.clear()
        self.output.insert(tk.END, "Lowest Score:\n\n")
        self.output.insert(tk.END, self.format_student(worst))

    #For Sorting The Students

    def sort_students(self):
        order = messagebox.askyesno("Sort", "Sort Ascending? (No = descending)")
        self.students.sort(key=lambda s: calc_total(s), reverse=not order)
        self.view_all()

    #Adding Students

    def add_student(self):
        try:
            num = int(simpledialog.askstring("Add", "Student Number (1000–9999):", parent=self.root))
            name = simpledialog.askstring("Add", "Student Name:", parent=self.root)
            c1 = int(simpledialog.askstring("Add", "Course Work 1 Marks (0-20)", parent=self.root))
            c2 = int(simpledialog.askstring("Add", "Course Work 2 Marks (0–20):", parent=self.root))
            c3 = int(simpledialog.askstring("Add", "Course Work 3 Marks (0–20):", parent=self.root))
            exam = int(simpledialog.askstring("Add", "Exam Mark (0–100):", parent=self.root))

            self.students.append({
                "Number": num,
                "Name": name,
                "C1": c1, "C2": c2, "C3": c3,
                "exam": exam
            })
            save_students(self.students)
            messagebox.showinfo("Success", "Student Successfully Added!")

        except:
            messagebox.showerror("Error", "Input Invalid")

    #Deleting A Student

    def delete_student(self):
        code = simpledialog.askstring("Delete", "Enter Student Name:")
        if not code:
            return
        before = len(self.students)
        self.students = [s for s in self.students if code.lower() not in s["Name"].lower() and code != str(s["Number"])]
        after = len(self.students)

        if before == after:
            messagebox.showinfo("Delete", "No Student Found.")
        else:
            save_students(self.students)
            messagebox.showinfo("Delete", "Student Deleted.")

    #Updating Student Info

    def update_student(self):
        code = simpledialog.askstring("Update", "Enter Student Number Or Name:")
        if not code:
            return

        matches = [s for s in self.students if code.lower() in s["Name"].lower() or code == str(s["Number"])]
        if not matches:
            messagebox.showinfo("Update", "No Student Found.")
            return

        s = matches[0]

        field = simpledialog.askstring("Update", "What Will You Update? (Name, C1, C2, C3, Exam)", parent=self.root)

        if field not in ["Name", "C1", "C2", "C3", "Exam"]:
            messagebox.showerror("Error", "Invalid field")
            return

        new_val = simpledialog.askstring("Update", f"Enter New {field}:", parent=self.root)
        if field == "Name":
            s["Name"] = new_val
        else:
            s[field] = int(new_val)

        save_students(self.students)
        messagebox.showinfo("Update", "Record Updated.")

root = tk.Tk()
icon = tk.PhotoImage(file="Assessment 1 - Skills Portfolio\A1 - Resources\Exercise 3 - Student Library\BSU Logo.png")
root.iconphoto(False, icon)
app = StudentManagerApp(root)
root.mainloop()