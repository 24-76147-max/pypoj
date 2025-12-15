import tkinter as tk
from tkinter import messagebox
import random

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


class ScienceQuizApp:
    def __init__(self, root):  # ✅ FIX 1
        self.root = root
        self.root.title("PySci Quiz")
        self.root.geometry("600x500")
        self.root.configure(bg="#E0F7FA")

        self.category = None
        self.questions = []
        self.current_question_index = 0
        self.score = 0
        self.selected_option = tk.StringVar()

        # Category frame
        self.category_frame = tk.Frame(root, bg="#E0F7FA")
        self.category_label = tk.Label(
            self.category_frame,
            text="Choose a fun topic!",
            font=("Comic Sans MS", 18, "bold"),
            bg="#E0F7FA",
            fg="#00796B"
        )
        self.category_label.pack(pady=20)

        tk.Button(
            self.category_frame,
            text="Physics (Things that Move!)",
            font=("Comic Sans MS", 14),
            bg="#FFEB3B",
            command=lambda: self.select_category("Physics")
        ).pack(pady=10, fill="x", padx=50)

        tk.Button(
            self.category_frame,
            text="Chemistry (Mixing and Changing!)",
            font=("Comic Sans MS", 14),
            bg="#FF9800",
            fg="white",
            command=lambda: self.select_category("Chemistry")
        ).pack(pady=10, fill="x", padx=50)

        tk.Button(
            self.category_frame,
            text="Biology (Living Things!)",
            font=("Comic Sans MS", 14),
            bg="#4CAF50",
            fg="white",
            command=lambda: self.select_category("Biology")
        ).pack(pady=10, fill="x", padx=50)

        self.category_frame.pack()

        # Question frame
        self.question_frame = tk.Frame(root, bg="#E0F7FA")
        self.question_label = tk.Label(
            self.question_frame,
            font=("Comic Sans MS", 16),
            wraplength=500,
            bg="#E0F7FA"
        )
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for _ in range(4):
            rb = tk.Radiobutton(
                self.question_frame,
                variable=self.selected_option,
                font=("Comic Sans MS", 14),
                bg="#E0F7FA"
            )
            rb.pack(anchor="w", pady=5)
            self.option_buttons.append(rb)

        tk.Button(
            self.question_frame,
            text="Submit My Answer!",
            font=("Comic Sans MS", 14),
            bg="#2196F3",
            fg="white",
            command=self.check_answer
        ).pack(pady=20)

    def select_category(self, category):
        self.category = category
        self.questions = quiz_data[category].copy()
        random.shuffle(self.questions)
        self.current_question_index = 0
        self.score = 0
        self.category_frame.pack_forget()
        self.question_frame.pack()
        self.display_question()

    def display_question(self):
        if self.current_question_index < len(self.questions):
            q = self.questions[self.current_question_index]
            self.question_label.config(text=q["question"])
            for i, option in enumerate(q["options"]):
                self.option_buttons[i].config(text=option, value=option)
            self.selected_option.set("")
        else:
            self.show_score()

    def check_answer(self):
        selected = self.selected_option.get()
        correct = self.questions[self.current_question_index]["answer"]

        if selected == correct:
            self.score += 1  # ✅ FIX 2
            messagebox.showinfo("Yay!", "Correct! You're a science star!")
        else:
            messagebox.showinfo("Oops!", f"The correct answer is {correct}")

        self.current_question_index += 1
        self.display_question()

    def show_score(self):
        messagebox.showinfo(
            "Quiz Done!",
            f"You scored {self.score} out of 5 in {self.category}!"
        )
        self.question_frame.pack_forget()
        self.category_frame.pack()


# ✅ FIX 3
if __name__ == "__main__":
    root = tk.Tk()
    app = ScienceQuizApp(root)
    root.mainloop()
