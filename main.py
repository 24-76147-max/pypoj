import tkinter as tk
from tkinter import messagebox
import random

quiz_data = {
    "Physics": [...],
    "Chemistry": [...],
    "Biology": [...]
}
 
 # ==============================
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
