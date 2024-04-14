import tkinter as tk
import sympy as sp
from tkinter import scrolledtext

class BisectionMethod:
    def __init__(self, a, b, function_inp, epsilon_error):
        self.a = a
        self.b = b
        self.x = sp.Symbol('x')
        self.function = sp.sympify(function_inp)
        self.epsilon_error = epsilon_error
        self.n = 1
        self.output = ""

    def calculate(self):
        self.c = (self.a + self.b) / 2
        self.epsilon = self.b - self.a

        while self.epsilon > self.epsilon_error:
            self.f_a = self.function.subs(self.x, self.a)
            self.f_b = self.function.subs(self.x, self.b)
            self.f_c = self.function.subs(self.x, self.c)

            self.print_values()

            if self.f_c > 0:
                self.b = self.c
            elif self.f_c < 0:
                self.a = self.c

            self.c = (self.a + self.b) / 2
            self.epsilon = self.b - self.a
            self.n += 1

        return self.output

    def print_values(self):
        self.output += f'\nn = {self.n}\n'
        self.output += f'f(a): {self.f_a}\n'
        self.output += f'f(b): {self.f_b}\n'
        self.output += f'C: {self.c}\n'
        self.output += f'f(c): {self.f_c}\n'
        self.output += f'b-a: {self.epsilon}\n'

def calculate():
    a = float(a_entry.get())
    b = float(b_entry.get())
    function_inp = function_entry.get()
    epsilon_error = float(epsilon_entry.get())

    bisection_method = BisectionMethod(a, b, function_inp, epsilon_error)
    output = bisection_method.calculate()
    result_text.insert(tk.END, output)

root = tk.Tk()
root.title("Bisection Method")

# a value entry
a_label = tk.Label(root, text="Enter value of a:")
a_label.grid(row=0, column=0, sticky="w")
a_entry = tk.Entry(root)
a_entry.grid(row=0, column=1, sticky="w")

# b value entry
b_label = tk.Label(root, text="Enter value of b:")
b_label.grid(row=1, column=0, sticky="w")
b_entry = tk.Entry(root)
b_entry.grid(row=1, column=1, sticky="w")

# function entry
function_label = tk.Label(root, text="Enter function:")
function_label.grid(row=2, column=0, sticky="w")
function_entry = tk.Entry(root)
function_entry.grid(row=2, column=1, sticky="w")

# epsilon error entry
epsilon_label = tk.Label(root, text="Enter epsilon error value:")
epsilon_label.grid(row=3, column=0, sticky="w")
epsilon_entry = tk.Entry(root)
epsilon_entry.grid(row=3, column=1, sticky="w")

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=4, column=1, pady=10)

# Result text
result_text = scrolledtext.ScrolledText(root, width=70, height=10)
result_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()