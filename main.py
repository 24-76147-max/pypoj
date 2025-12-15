import tkinter as tk
from tkinter import messagebox
import random

# ==============================
# 1. Quiz Data (this is your "database")
# ==============================
# Define the quiz data (simplified for elementary level)
quiz_data = {
    "Physics": [
        {
            "question": "What makes things fall down to the ground?",
            "options": ["Wind", "Gravity", "Sunlight", "Water"],
            "answer": "Gravity"
        },
        {
            "question": "What do we use to see in the dark?",
            "options": ["A flashlight", "A rock", "A tree", "A cloud"],
            "answer": "A flashlight"
        },
        {
            "question": "What is the color of the sky on a sunny day?",
            "options": ["Green", "Blue", "Red", "Yellow"],
            "answer": "Blue"
        },
        {
            "question": "What happens when you push a swing?",
            "options": ["It stops", "It goes higher", "It disappears", "It turns into a ball"],
            "answer": "It goes higher"
        },
        {
            "question": "What is hot and comes from the sun?",
            "options": ["Rain", "Snow", "Light", "Wind"],
            "answer": "Light"
        }
    ],
    "Chemistry": [
        {
            "question": "What is water made of?",
            "options": ["Sand", "Hydrogen and Oxygen", "Rocks", "Air"],
            "answer": "Hydrogen and Oxygen"
        },
        {
            "question": "What do we call the stuff that makes bubbles in soap?",
            "options": ["Sugar", "Soap", "Salt", "Pepper"],
            "answer": "Soap"
        },
        {
            "question": "What color is the flame of a candle?",
            "options": ["Blue", "Orange", "Green", "Purple"],
            "answer": "Orange"
        },
        {
            "question": "What happens when you mix blue and yellow paint?",
            "options": ["Red", "Green", "Purple", "Black"],
            "answer": "Green"
        },
        {
            "question": "What is ice made from?",
            "options": ["Fire", "Water", "Earth", "Wind"],
            "answer": "Water"
        }
    ],
    "Biology": [
        {
            "question": "What do plants need to grow?",
            "options": ["Darkness", "Sunlight and water", "Rocks", "Fire"],
            "answer": "Sunlight and water"
        },
        {
            "question": "How many legs does a spider have?",
            "options": ["6", "8", "4", "10"],
            "answer": "8"
        },
        {
            "question": "What is the biggest animal in the ocean?",
            "options": ["Shark", "Whale", "Fish", "Dolphin"],
            "answer": "Whale"
        },
        {
            "question": "What do caterpillars turn into?",
            "options": ["Birds", "Butterflies", "Frogs", "Snakes"],
            "answer": "Butterflies"
        },
        {
            "question": "Which part of the body helps you see?",
            "options": ["Ears", "Eyes", "Nose", "Mouth"],
            "answer": "Eyes"
        }
    ]
}


# ==============================
# 2. Main App Class
# ==============================
class ScienceQuizApp:

    # Initialize the program
    def __init__(self, root):
        self.root = root
        self.root.title("Fun Elementary Science Quiz")
        self.root.geometry("600x500")
        self.root.configure(bg="#E0F7FA")

        self.questions = []
        self.current_question_index = 0
        self.score = 0
        self.selected_option = tk.StringVar()

        # --------------------------
        # Category Selection Screen
        # --------------------------
        self.category_frame = tk.Frame(root, bg="#E0F7FA")

        tk.Label(
            self.category_frame,
            text="Choose a fun topic!",
            font=("Comic Sans MS", 18, "bold"),
            bg="#E0F7FA"
        ).pack(pady=20)

        tk.Button(
            self.category_frame,
            text="Physics",
            font=("Comic Sans MS", 14),
            command=lambda: self.select_category("Physics")
        ).pack(pady=10)

        tk.Button(
            self.category_frame,
            text="Chemistry",
            font=("Comic Sans MS", 14),
            command=lambda: self.select_category("Chemistry")
        ).pack(pady=10)

        tk.Button(
            self.category_frame,
            text="Biology",
            font=("Comic Sans MS", 14),
            command=lambda: self.select_category("Biology")
        ).pack(pady=10)

        self.category_frame.pack()

        # --------------------------
        # Question Screen
        # --------------------------
        self.question_frame = tk.Frame(root, bg="#E0F7FA")

        self.question_label = tk.Label(
            self.question_frame,
            font=("Comic Sans MS", 16),
            wraplength=500,
            bg="#E0F7FA"
        )
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(
                self.question_frame,
                text="",
                variable=self.selected_option,
                value="",
                font=("Comic Sans MS", 14),
                bg="#E0F7FA"
            )
            rb.pack(anchor="w", pady=5)
            self.option_buttons.append(rb)

        tk.Button(
            self.question_frame,
            text="Submit Answer",
            font=("Comic Sans MS", 14),
            command=self.check_answer
        ).pack(pady=20)

    # ==============================
    # 3. When a category is chosen
    # ==============================
    def select_category(self, category):
        self.questions = quiz_data[category]
        random.shuffle(self.questions)
        self.current_question_index = 0
        self.score = 0

        self.category_frame.pack_forget()
        self.question_frame.pack()

        self.load_question()

    # ==============================
    # 4. Load a question
    # ==============================
    def load_question(self):
        self.selected_option.set("")

        question_data = self.questions[self.current_question_index]
        self.question_label.config(text=question_data["question"])

        for i, option in enumerate(question_data["options"]):
            self.option_buttons[i].config(
                text=option,
                value=option
            )

    # ==============================
    # 5. Check the answer
    # ==============================
    def check_answer(self):
        selected = self.selected_option.get()
        correct = self.questions[self.current_question_index]["answer"]

        if selected == "":
            messagebox.showwarning("Oops!", "Please choose an answer!")
            return

        if selected == correct:
            self.score += 1
            messagebox.showinfo("Correct!", "Good job! 🎉")
        else:
            messagebox.showinfo("Oops!", f"The correct answer is: {correct}")

        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            self.load_question()
        else:
            messagebox.showinfo(
                "Quiz Finished!",
                f"You scored {self.score} out of {len(self.questions)}"
            )
            self.question_frame.pack_forget()
            self.category_frame.pack()

# ==============================
# 6. Start the Program
# ==============================
root = tk.Tk()
app = ScienceQuizApp(root)
root.mainloop()
