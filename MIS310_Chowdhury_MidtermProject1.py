from tkinter import *
from tkinter import messagebox

score_list = []

def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

def add_score():
    try:
        score = float(entry_score.get())
        if score < 0 or score > 100:
            messagebox.showerror("Error", "Score must be between 0 and 100.")
            return
        score_list.append(score)
        listbox.insert(END, f"Score {len(score_list)}: {score}")
        entry_score.delete(0, END)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def calculate():
    if len(score_list) == 0:
        messagebox.showwarning("Warning", "No scores entered.")
        return
    total = 0
    for s in score_list:
        total += s
    avg = total / len(score_list)
    label_result.config(text=f"Average: {avg:.2f}  |  Grade: {get_grade(avg)}")

def clear_all():
    score_list.clear()
    listbox.delete(0, END)
    label_result.config(text="Average: --  |  Grade: --")
    entry_score.delete(0, END)
window = Tk()
window.title("Student Grades")
window.geometry("400x450")
window.resizable(0, 0)
window.config(bg="light blue")
Label(window, text="Student Grades", font=("Arial", 16, "bold"), bg="light blue").pack(pady=10)
Label(window, text="Enter Score (0-100):", font=("Arial", 11), bg="light blue").pack()
entry_score = Entry(window, font=("Arial", 12), width=10, justify="center")
entry_score.pack(pady=5)

Button(window, text="Add Score", bg="light green", width=12, command=add_score).pack(pady=3)

listbox = Listbox(window, font=("Arial", 11), height=6, width=25)
listbox.pack(pady=5)

Button(window, text="Calculate Grade", bg="light green", width=14, command=calculate).pack(pady=3)
Button(window, text="Clear All", bg="#ffcccc", width=14, command=clear_all).pack(pady=3)
label_result = Label(window, text="Average: --  |  Grade: --", font=("Arial", 12, "bold"), bg="light blue")
label_result.pack(pady=10)

window.mainloop()