import tkinter as tk

class PatternLockUI:
    def __init__(self, master, on_complete):
        self.master = master
        self.on_complete = on_complete
        self.pattern = []
        self.buttons = []

        self.master.title("Pattern Lock")
        self.master.geometry("250x300")

        self.canvas = tk.Frame(master)
        self.canvas.pack()

        for i in range(9):
            btn = tk.Button(self.canvas, text=str(i+1), width=6, height=3,
                            command=lambda i=i: self.add_to_pattern(i+1))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

        self.submit_btn = tk.Button(master, text="Submit", command=self.submit)
        self.submit_btn.pack(pady=10)

    def add_to_pattern(self, num):
        if num not in self.pattern:
            self.pattern.append(num)
            self.buttons[num-1].config(state="disabled", bg="lightblue")

    def submit(self):
        if self.pattern:
            self.on_complete(self.pattern)
        else:
            print("No pattern entered.")
