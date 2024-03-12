import tkinter as tk
from sympy import symbols, diff, acos, N
import numpy as np

def calculate_higher_derivative(c, n):
    x = symbols('x')
    expression = acos(x)
    higher_derivative = diff(expression, x, n)
    result = N(higher_derivative.subs(x, c))
    return result

def calculate_true_value(true_val):
    x = symbols('x')
    expression = acos(x)
    result = N(expression.subs(x, true_val))
    return result

def on_calculate():
    c_value = float(entry_c.get())
    n_value = int(entry_n.get())
    true_val = float(entry_true_val.get())

    higher_derivative_result = calculate_higher_derivative(c_value, n_value)
    true_value_result = calculate_true_value(true_val)

    result_label.config(text=f"Higher Derivative: {higher_derivative_result}\nTrue Value: {true_value_result}")

# Create the main window
root = tk.Tk()
root.title("Arccos(x) Derivative Calculator")

# Create and place widgets
label_c = tk.Label(root, text="Enter 'c' (-1 < c < 1):")
label_c.pack()

entry_c = tk.Entry(root)
entry_c.pack()

label_n = tk.Label(root, text="Enter 'n' (number of derivatives):")
label_n.pack()

entry_n = tk.Entry(root)
entry_n.pack()

label_true_val = tk.Label(root, text="Enter 'true_val' for substitution:")
label_true_val.pack()

entry_true_val = tk.Entry(root)
entry_true_val.pack()

calculate_button = tk.Button(root, text="Calculate", command=on_calculate)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Run the main loop
root.mainloop()
