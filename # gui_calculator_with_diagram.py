# gui_calculator_with_diagram.py
# Run korlei: terminal-e diagram print hobe -> tarpor calculator window open hobe.

import tkinter as tk
from tkinter import messagebox
import math

DIAGRAM = r"""
+-----------------------------------+
|         PYTHON CALCULATOR         |
+-----------------------------------+
|  [  display area — expression ]   |
+-----------------------------------+
|  C  |  ⌫  |  %  |  /   |
|  7  |  8  |  9  |  *   |
|  4  |  5  |  6  |  -   |
|  1  |  2  |  3  |  +   |
|  ^  |  0  |  .  |  =   |
+-----------------------------------+
"""

def print_design_diagram():
    # Terminal-e layout idea print korbe
    print(DIAGRAM)

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Calculator")
        self.geometry("340x450")
        self.configure(bg="#1a1a1a")
        self.resizable(False, False)

        # expression holder
        self.expr = tk.StringVar()

        # display entry
        entry = tk.Entry(
            self,
            textvariable=self.expr,
            font=("Segoe UI", 22, "bold"),
            bd=8,
            relief=tk.FLAT,
            bg="#333",
            fg="#fff",
            justify="right",
            insertbackground="white"
        )
        entry.pack(fill="x", padx=12, pady=12, ipady=15)

        # buttons layout
        buttons = [
            ["C", "⌫", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["^", "0", ".", "="],
        ]

        frame = tk.Frame(self, bg="#1a1a1a")
        frame.pack(expand=True, fill="both", padx=12, pady=12)

        for r, row in enumerate(buttons):
            for c, label in enumerate(row):
                btn = tk.Button(
                    frame,
                    text=label,
                    font=("Segoe UI", 16, "bold"),
                    width=4,
                    height=2,
                    relief=tk.FLAT,
                    bg="#444",
                    fg="white",
                    activebackground="#666",
                    activeforeground="white",
                    command=lambda v=label: self.on_press(v)
                )
                btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

        for i in range(4):
            frame.grid_columnconfigure(i, weight=1)
        for i in range(5):
            frame.grid_rowconfigure(i, weight=1)

        # keyboard shortcuts
        self.bind("<Return>", lambda e: self.on_press("="))
        self.bind("<BackSpace>", lambda e: self.on_press("⌫"))
        self.bind("<Escape>", lambda e: self.on_press("C"))

    def on_press(self, key):
        if key == "C":
            self.expr.set("")
        elif key == "⌫":
            self.expr.set(self.expr.get()[:-1])
        elif key == "=":
            self.calculate()
        else:
            # add the pressed key to expression
            self.expr.set(self.expr.get() + key)

    def calculate(self):
        raw = self.expr.get()
        # ^ ke power operator (Python: **) e convert korchi
        safe = raw.replace("^", "**")
        try:
            # allowed characters check (basic safety)
            allowed = "0123456789.+-*/()% "
            if any(ch not in allowed for ch in safe):
                raise ValueError("Invalid characters in expression.")
            # eval with no builtins
            result = eval(safe, {"__builtins__": None}, {})
            self.expr.set(str(result))
        except Exception:
            messagebox.showerror("Error", "Invalid Expression!")

if __name__ == "__main__":
    print_design_diagram()   # terminal-e design diagram dekhabe
    app = Calculator()       # app ready
    app.mainloop()          # window open kore
