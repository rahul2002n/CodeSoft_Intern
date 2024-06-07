import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_var.get())
    include_upper = upper_var.get()
    include_lower = lower_var.get()
    include_digits = digits_var.get()
    include_symbols = symbols_var.get()

    char_pool = ""
    if include_upper:
        char_pool += string.ascii_uppercase
    if include_lower:
        char_pool += string.ascii_lowercase
    if include_digits:
        char_pool += string.digits
    if include_symbols:
        char_pool += string.punctuation

    if not char_pool:
        messagebox.showwarning("Warning", "Select at least one character type!")
        return

    password = ''.join(random.choice(char_pool) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

root = tk.Tk()
root.title("Password Generator")

length_var = tk.StringVar(value="12")
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

frame = tk.Frame(root, padx=30, pady=30)
frame.pack(padx=20, pady=30)

tk.Label(frame, text="Password Length:").grid(row=0, column=0, sticky="w")
length_entry = tk.Entry(frame, textvariable=length_var, width=5)
length_entry.grid(row=0, column=1, sticky="w")

tk.Checkbutton(frame, text="Include Uppercase Letters", variable=upper_var).grid(row=1, column=0, columnspan=2, sticky="w")
tk.Checkbutton(frame, text="Include Lowercase Letters", variable=lower_var).grid(row=2, column=0, columnspan=2, sticky="w")
tk.Checkbutton(frame, text="Include Digits", variable=digits_var).grid(row=3, column=0, columnspan=2, sticky="w")
tk.Checkbutton(frame, text="Include Symbols", variable=symbols_var).grid(row=4, column=0, columnspan=2, sticky="w")

tk.Label(frame, text="Generated Password:").grid(row=5, column=0, sticky="w")
password_entry = tk.Entry(frame, width=30)
password_entry.grid(row=5, column=1, sticky="w")

generate_button = tk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
