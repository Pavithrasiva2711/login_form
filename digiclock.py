import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%A, %d %B %Y")
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    time_label.after(1000, update_time)

root = tk.Tk()
root.title("💠 Digital Clock")

window_width = 550
window_height = 220
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg="#0f172a")  

frame = tk.Frame(root, bg="#0f172a", bd=5, relief="flat")
frame.pack(padx=25, pady=25)

border = tk.Frame(frame, bg="#00ffff", padx=3, pady=3)
border.pack()

display = tk.Frame(border, bg="#1e293b", padx=30, pady=20)
display.pack()

time_label = tk.Label(display, font=("Consolas", 50, "bold"), bg="#1e293b", fg="#00FFFF")
time_label.pack()

date_label = tk.Label(display, font=("Segoe UI", 20), bg="#1e293b", fg="#e2e8f0")
date_label.pack(pady=(10, 0))

update_time()
root.mainloop()
