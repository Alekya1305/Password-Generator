import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def on_generate():
    password = generate_password()
    entry_password.config(state="normal")
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)
    entry_password.config(state="readonly")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.configure(bg="#2C3E50")

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10)
style.configure("TEntry", font=("Arial", 12))

label_title = tk.Label(root, text="Secure Password Generator", font=("Arial", 14, "bold"), fg="white", bg="#2C3E50")
label_title.pack(pady=10)

btn_generate = ttk.Button(root, text="Generate Password", command=on_generate)
btn_generate.pack(pady=10)

entry_password = ttk.Entry(root, width=30, state="readonly", justify="center")
entry_password.pack(pady=10)

root.mainloop()