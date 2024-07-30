import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate a random password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Function to handle the password generation process
def on_generate():
    try:
        length = int(entry.get())
        if length < 1:
            messagebox.showwarning("Invalid Input", "Password length must be at least 1.")
        else:
            password = generate_password(length)
            result_label.config(text=f"Generated password: {password}", fg="blue")
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Colorful Password Generator")
root.geometry("400x300")
root.config(bg="#f0f0f0")

# Create and place the widgets with colors
tk.Label(root, text="Enter the desired length of the password:", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)
entry = tk.Entry(root, font=("Arial", 14), bd=2, relief="solid")
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", font=("Arial", 14), bg="#4CAF50", fg="white", command=on_generate)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0")
result_label.pack(pady=10)

# Run the main event loop
root.mainloop()
