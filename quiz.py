import tkinter as tk
from tkinter import messagebox
import random
quiz_questions = [
    {
        "question": "In which year was Prophet Muhammad (PBUH) born?",
        "choices": ["A. 570 CE", "B. 580 CE", "C. 590 CE", "D. 600 CE"],
        "answer": "A"
    },
    {
        "question": "In which city was Prophet Muhammad (PBUH) born?",
        "choices": ["A. Medina", "B. Mecca", "C. Jerusalem", "D. Cairo"],
        "answer": "B"
    },
    {
        "question": "What was the name of Prophet Muhammad's (PBUH) first wife?",
        "choices": ["A. Aisha", "B. Khadijah", "C. Fatimah", "D. Zainab"],
        "answer": "B"
    },
    {
        "question": "How old was Prophet Muhammad (PBUH) when he received the first revelation?",
        "choices": ["A. 30 years old", "B. 35 years old", "C. 40 years old", "D. 45 years old"],
        "answer": "C"
    },
    {
        "question": "What is the name of the cave where Prophet Muhammad (PBUH) received his first revelation?",
        "choices": ["A. Cave Hira", "B. Cave Thawr", "C. Cave Saur", "D. Cave Noor"],
        "answer": "A"
    },
    {
        "question": "What was the name of Prophet Muhammad's (PBUH) mother?",
        "choices": ["A. Amina", "B. Aminah", "C. Amin", "D. Amna"],
        "answer": "B"
    },
    {
        "question": "What was the name of Prophet Muhammad's (PBUH) father?",
        "choices": ["A. Abdullah", "B. Abdul Muttalib", "C. Abu Talib", "D. Abu Bakr"],
        "answer": "A"
    },
    {
        "question": "What is the name of the migration of Prophet Muhammad (PBUH) from Mecca to Medina called?",
        "choices": ["A. Hajj", "B. Umrah", "C. Hijrah", "D. Iftar"],
        "answer": "C"
    },
    {
        "question": "How many years did Prophet Muhammad (PBUH) preach in Mecca before migrating to Medina?",
        "choices": ["A. 10 years", "B. 11 years", "C. 12 years", "D. 13 years"],
        "answer": "D"
    },
    {
        "question": "In which battle did Prophet Muhammad (PBUH) first participate?",
        "choices": ["A. Battle of Badr", "B. Battle of Uhud", "C. Battle of Khandaq", "D. Battle of Hunayn"],
        "answer": "A"
    },
    {
        "question": "How many battles did Prophet Muhammad (PBUH) personally participate in?",
        "choices": ["A. 27", "B. 25", "C. 23", "D. 21"],
        "answer": "A"
    },
    {
        "question": "What is the name of the treaty that Prophet Muhammad (PBUH) signed with the Quraish tribe?",
        "choices": ["A. Treaty of Hudaybiyyah", "B. Treaty of Hudaibiyya", "C. Treaty of Hudaibiya", "D. Treaty of Hudaybiya"],
        "answer": "A"
    },
    {
        "question": "What is the name of the night journey that Prophet Muhammad (PBUH) undertook from Mecca to Jerusalem?",
        "choices": ["A. Isra and Mi'raj", "B. Isra and Meraj", "C. Isra and Miraj", "D. Isra and Mairaj"],
        "answer": "A"
    },
    {
        "question": "In which year did Prophet Muhammad (PBUH) pass away?",
        "choices": ["A. 620 CE", "B. 630 CE", "C. 632 CE", "D. 634 CE"],
        "answer": "C"
    },
    {
        "question": "Who was the first caliph after Prophet Muhammad's (PBUH) death?",
        "choices": ["A. Umar ibn al-Khattab", "B. Uthman ibn Affan", "C. Ali ibn Abi Talib", "D. Abu Bakr as-Siddiq"],
        "answer": "D"
    },
    {
        "question": "What is the name of Prophet Muhammad's (PBUH) paternal grandfather?",
        "choices": ["A. Abdul Muttalib", "B. Abu Talib", "C. Abdullah", "D. Hamza"],
        "answer": "A"
    },
    {
        "question": "How many children did Prophet Muhammad (PBUH) have?",
        "choices": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "D"
    },
    {
        "question": "Which angel brought the first revelation to Prophet Muhammad (PBUH)?",
        "choices": ["A. Angel Jibril (Gabriel)", "B. Angel Mikail (Michael)", "C. Angel Israfil", "D. Angel Azrael"],
        "answer": "A"
    },
    {
        "question": "What is the name of the tribe that Prophet Muhammad (PBUH) belonged to?",
        "choices": ["A. Banu Hashim", "B. Banu Umayya", "C. Banu Makhzum", "D. Banu Zuhra"],
        "answer": "A"
    },
    {
        "question": "What was the occupation of Prophet Muhammad (PBUH) before prophethood?",
        "choices": ["A. Shepherd", "B. Merchant", "C. Carpenter", "D. Farmer"],
        "answer": "B"
    }
]
current_question_index = 0
score = 0
root = tk.Tk()
root.title("Prophet Muhammad (PBUH) Quiz Game")
def display_question():
    global current_question_index
    question = quiz_questions[current_question_index]
    
    # Update question label
    question_label.config(text=question["question"])
    
    # Update choice buttons
    for i, choice in enumerate(question["choices"]):
        choice_buttons[i].config(text=choice)
def check_answer(selected_choice):
    global current_question_index, score
    
    question = quiz_questions[current_question_index]
    correct_answer = question["answer"]
    
    if selected_choice == correct_answer:
        score += 1
    
    current_question_index += 1
    
    if current_question_index < len(quiz_questions):
        display_question()
    else:
        display_final_results()
def display_final_results():
    global score
    messagebox.showinfo("Quiz Finished", f"Your final score is {score} out of {len(quiz_questions)}.")
    root.destroy()
welcome_label = tk.Label(root, text="Welcome to the Prophet Muhammad (PBUH) Quiz Game!", font=("Arial", 16))
welcome_label.pack(pady=20)

question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400)
question_label.pack(pady=20)

choice_buttons = []
for i in range(4):
    btn = tk.Button(root, text="", font=("Arial", 12), width=40, command=lambda i=i: check_answer(quiz_questions[current_question_index]["choices"][i][0]))
    btn.pack(pady=5)
    choice_buttons.append(btn)
random.shuffle(quiz_questions)
display_question()
root.mainloop()
