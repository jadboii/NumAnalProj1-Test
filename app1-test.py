import numpy as np
import sympy as sp
import tkinter as tk
from tkinter import ttk
from scipy.special import factorial
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter.simpledialog as sdg

def factor(n):
    if n == 0:
        return 1
    else:
        return n * factor(n - 1)

def arccos_taylor_series(x, n):
    x = float(x)
    n = int(n)
    series_sum = 0
    for k in range(n):
        term = ((-1) ** k) * (factor(2 * k) / (2 ** (2 * k) * factor(k) * factor(2 * k + 1))) * x ** (2 * k + 1)
        series_sum += term
    return series_sum


def calculate_errors(series_sum, x, n):
    x = float(x)
    n = int(n)
    exact_value = np.arccos(x)
    approx_value = arccos_taylor_series(x, n)
    absolute = abs(series_sum - approx_value)
    absolute_error = absolute * 100
    relative_error = round(absolute_error / abs(series_sum), 2)
    return absolute_error, relative_error

def insert_constant_value(constant):
    entry_x.delete(0, tk.END)
    entry_x.insert(0, constant)

def solve_button_clicked():
    x_value = entry_x.get()
    n_value = entry_n.get()

    try:
        x_value = float(x_value)
        n_value = int(n_value)
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")
        return

    series_sum = arccos_taylor_series(x_value, n_value)
    absolute_error, relative_error = calculate_errors(series_sum, x_value, n_value)

    result_label.config(text=f"Result: {series_sum}")
    absolute_error_label.config(text=f"Absolute Error: {absolute_error}%")
    relative_error_label.config(text=f"Relative Error: {relative_error}%")

    # Update the plot
    plot_taylor_series(x_value, n_value)

def plot_taylor_series(x, n):
    x_vals = np.linspace(-1, 1, 100)
    y_vals_exact = np.arccos(x_vals)
    y_vals_approx = [arccos_taylor_series(xi, n) for xi in x_vals]

    ax.clear()
    ax.plot(x_vals, y_vals_exact, label='Exact arccos(x)')
    ax.plot(x_vals, y_vals_approx, label=f'Taylor Series (n={n})')
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Arccos(x) Taylor Series Approximation')

    canvas.draw()

def solve_fraction():
    numerator = sdg.askfloat("Fraction", "Enter the numerator:")
    denominator = sdg.askfloat("Fraction", "Enter the denominator:")

    if numerator is not None and denominator is not None and denominator != 0:
        fraction_value = numerator / denominator
        entry_x.delete(0, tk.END)
        entry_x.insert(0, fraction_value)
    else:
        result_label.config(text="Invalid fraction input. Please enter valid numbers.")


def solve_sqrt():
    value = sdg.askfloat("Square Root", "Enter the value for square root:")

    if value is not None and value >= 0:  # Ensure non-negative input
        sqrt_value = sp.sqrt(value)  # Using sympy for accurate square root
        entry_x.delete(0, tk.END)
        entry_x.insert(0, sqrt_value.evalf())  # Evaluate the square root value
    else:
        result_label.config(text="Invalid square root input. Please enter a non-negative number.")


# GUI setup
root = tk.Tk()
root.title("Arccos(x) Taylor Series Solver")

# Input fields and labels
label_x = tk.Label(root, text="Enter x:")
entry_x = tk.Entry(root)

label_n = tk.Label(root, text="Enter n:")
entry_n = tk.Entry(root)

# Buttons
solve_button = tk.Button(root, text="Solve", command=solve_button_clicked)

pi_button = tk.Button(root, text="π", command=lambda: insert_constant_value(np.pi))
fraction_button = tk.Button(root, text="Fraction", command=solve_fraction)
e_button = tk.Button(root, text="e", command=lambda: insert_constant_value(np.e))
sqrt_button = tk.Button(root, text="√", command=solve_sqrt)

# Result labels
result_label = tk.Label(root, text="Result:")
absolute_error_label = tk.Label(root, text="Absolute Error:")
relative_error_label = tk.Label(root, text="Relative Error:")

# Matplotlib setup
fig, ax = plt.subplots(figsize=(5, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=0, column=3, rowspan=8)

# Layout
label_x.grid(row=0, column=0, padx=5, pady=5)
entry_x.grid(row=0, column=1, padx=5, pady=5)

label_n.grid(row=1, column=0, padx=5, pady=5)
entry_n.grid(row=1, column=1, padx=5, pady=5)

solve_button.grid(row=2, column=0, columnspan=2, pady=10)

pi_button.grid(row=3, column=0, pady=5)
fraction_button.grid(row=3, column=1, pady=5)
e_button.grid(row=4, column=0, pady=5)
sqrt_button.grid(row=4, column=1, pady=5)

result_label.grid(row=5, column=0, columnspan=2, pady=5)
absolute_error_label.grid(row=6, column=0, columnspan=2, pady=5)
relative_error_label.grid(row=7, column=0, columnspan=2, pady=5)

# Main loop
root.mainloop()
