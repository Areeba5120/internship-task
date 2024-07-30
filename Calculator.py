import tkinter as tk
from tkinter import messagebox
def create_main_window():
    window = tk.Tk()
    window.title("Simple Calculator")
    window.geometry("400x500")
    window.resizable(False, False)
    return window
def create_display(window):
    display = tk.Entry(window, font=("Arial", 24), borderwidth=2, relief="solid")
    display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    return display
def button_click(display, value):
    current_text = display.get()
    if value == "=":
        try:
            result = str(eval(current_text))
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            display.delete(0, tk.END)
    elif value == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, value)
def create_buttons(window, display):
    button_texts = [
        "7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        "0", "C", "=", "+"
    ]

    row_val = 1
    col_val = 0

    for text in button_texts:
        button = tk.Button(window, text=text, font=("Arial", 18), borderwidth=1, relief="solid",
                           command=lambda t=text: button_click(display, t))
        button.grid(row=row_val, column=col_val, ipadx=20, ipady=20, padx=5, pady=5)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1
def main():
    window = create_main_window()
    display = create_display(window)
    create_buttons(window, display)
    window.mainloop()
if __name__ == "__main__":
    main()