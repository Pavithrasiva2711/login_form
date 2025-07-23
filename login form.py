import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Login Page")
root.geometry("400x420")
root.configure(bg="#dbeafe")  

frame = tk.Frame(root, bg="white", bd=0, relief="flat", padx=30, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")

title = tk.Label(frame, text="Welcome to MyApp", font=("Segoe UI", 18, "bold"), fg="#1e3a8a", bg="white")
title.pack(pady=(10, 5))
underline = tk.Frame(frame, bg="#1e3a8a", height=2, width=200)
underline.pack(pady=(0, 15))

tk.Label(frame, text="Username", font=("Segoe UI", 11), bg="white", anchor="w").pack(fill="x")
username_entry = tk.Entry(frame, font=("Segoe UI", 11), bg="#f1f5f9", bd=0, relief="flat")
username_entry.pack(fill="x", pady=(0, 15), ipady=8)

tk.Label(frame, text="Password", font=("Segoe UI", 11), bg="white", anchor="w").pack(fill="x")
password_entry = tk.Entry(frame, font=("Segoe UI", 11), show="*", bg="#f1f5f9", bd=0, relief="flat")
password_entry.pack(fill="x", pady=(0, 15), ipady=8)

def toggle_password():
    if password_entry.cget('show') == '*':
        password_entry.config(show='')
        toggle_btn.config(text="🙈 Hide")
    else:
        password_entry.config(show='*')
        toggle_btn.config(text="👁 Show")

toggle_btn = tk.Button(frame, text="👁 Show", command=toggle_password, bg="#e0e7ff", fg="#1e3a8a", relief="flat", font=("Segoe UI", 9))
toggle_btn.pack(pady=(0, 10))

remember_var = tk.IntVar()
tk.Checkbutton(frame, text="Remember Me", variable=remember_var, bg="white", font=("Segoe UI", 9)).pack(anchor="w")

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "Pavithra" and password == "pavi123":
        messagebox.showinfo("Login Successful", "Welcome, Pavithra!")
    else:
        messagebox.showerror("Error", "Incorrect Username or Password")

def clear_fields():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

btn_frame = tk.Frame(frame, bg="white")
btn_frame.pack(pady=20)

login_btn = tk.Button(btn_frame, text="Login", command=login, bg="#2563eb", fg="white", activebackground="#1e40af", activeforeground="white", font=("Segoe UI", 10, "bold"), width=12, relief="flat")
login_btn.grid(row=0, column=0, padx=5)

clear_btn = tk.Button(btn_frame, text="Clear", command=clear_fields, bg="#f59e0b", fg="white", activebackground="#b45309", activeforeground="white", font=("Segoe UI", 10, "bold"), width=12, relief="flat")
clear_btn.grid(row=0, column=1, padx=5)

root.mainloop()
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Login Page")
root.geometry("400x420")
root.configure(bg="#dbeafe") 

frame = tk.Frame(root, bg="white", bd=0, relief="flat", padx=30, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")

title = tk.Label(frame, text="Welcome to MyApp", font=("Segoe UI", 18, "bold"), fg="#1e3a8a", bg="white")
title.pack(pady=(10, 5))
underline = tk.Frame(frame, bg="#1e3a8a", height=2, width=200)
underline.pack(pady=(0, 15))

tk.Label(frame, text="Username", font=("Segoe UI", 11), bg="white", anchor="w").pack(fill="x")
username_entry = tk.Entry(frame, font=("Segoe UI", 11), bg="#f1f5f9", bd=0, relief="flat")
username_entry.pack(fill="x", pady=(0, 15), ipady=8)

tk.Label(frame, text="Password", font=("Segoe UI", 11), bg="white", anchor="w").pack(fill="x")
password_entry = tk.Entry(frame, font=("Segoe UI", 11), show="*", bg="#f1f5f9", bd=0, relief="flat")
password_entry.pack(fill="x", pady=(0, 15), ipady=8)

def toggle_password():
    if password_entry.cget('show') == '*':
        password_entry.config(show='')
        toggle_btn.config(text="🙈 Hide")
    else:
        password_entry.config(show='*')
        toggle_btn.config(text="👁 Show")

toggle_btn = tk.Button(frame, text="👁 Show", command=toggle_password, bg="#e0e7ff", fg="#1e3a8a", relief="flat", font=("Segoe UI", 9))
toggle_btn.pack(pady=(0, 10))

remember_var = tk.IntVar()
tk.Checkbutton(frame, text="Remember Me", variable=remember_var, bg="white", font=("Segoe UI", 9)).pack(anchor="w")

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "Pavithra" and password == "pavi123":
        messagebox.showinfo("Login Successful", "Welcome, Pavithra!")
    else:
        messagebox.showerror("Error", "Incorrect Username or Password")

def clear_fields():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

btn_frame = tk.Frame(frame, bg="white")
btn_frame.pack(pady=20)

login_btn = tk.Button(btn_frame, text="Login", command=login, bg="#2563eb", fg="white", activebackground="#1e40af", activeforeground="white", font=("Segoe UI", 10, "bold"), width=12, relief="flat")
login_btn.grid(row=0, column=0, padx=5)

clear_btn = tk.Button(btn_frame, text="Clear", command=clear_fields, bg="#f59e0b", fg="white", activebackground="#b45309", activeforeground="white", font=("Segoe UI", 10, "bold"), width=12, relief="flat")
clear_btn.grid(row=0, column=1, padx=5)

root.mainloop()
