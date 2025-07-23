import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get().replace("×", "*").replace("÷", "/")))
            screen.set(result)
        except:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    elif text == "←":
        screen.set(screen.get()[:-1])
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")
root.configure(bg="black")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 24", bd=10, relief="sunken", justify="right")
entry.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=10)

btns = [
    ["C", "←", "÷", "×"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", ".", "", ""]
]

for row in btns:
    frame = tk.Frame(root, bg="black")
    frame.pack(expand=True, fill="both")
    for btn in row:
        if btn != "":
            b = tk.Button(frame, text=btn, font="Arial 20 bold", relief="groove",
                          fg="white", bg="#333", activebackground="#555", padx=20, pady=20)
            b.pack(side="left", expand=True, fill="both", padx=5, pady=5)
            b.bind("<Button-1>", click)

root.mainloop()
