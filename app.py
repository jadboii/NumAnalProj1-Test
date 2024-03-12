import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class TaylorSeriesSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Taylor Series Solver")

        self.x_value = tk.StringVar(value="0")
        self.n_value = tk.StringVar(value="5")
        self.result_var = tk.StringVar()
        self.relative_error_var = tk.StringVar()
        self.absolute_error_var = tk.StringVar()

        # Define symbols i and term globally
        self.i, self.term = sp.symbols('i term')

        self.create_widgets()

    def create_widgets(self):
        # Entry for x value
        x_label = ttk.Label(self.root, text="Enter x:")
        x_entry = ttk.Entry(self.root, textvariable=self.x_value)
        x_label.grid(row=0, column=0, padx=5, pady=5)
        x_entry.grid(row=0, column=1, padx=5, pady=5)

        # Entry for n value
        n_label = ttk.Label(self.root, text="Enter n:")
        n_entry = ttk.Entry(self.root, textvariable=self.n_value)
        n_label.grid(row=1, column=0, padx=5, pady=5)
        n_entry.grid(row=1, column=1, padx=5, pady=5)

        # Solve Button
        solve_button = ttk.Button(self.root, text="Solve", command=self.solve_taylor_series)
        solve_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Result Label
        result_label = ttk.Label(self.root, text="Result:")
        result_value_label = ttk.Label(self.root, textvariable=self.result_var)
        result_label.grid(row=3, column=0, pady=5)
        result_value_label.grid(row=3, column=1, pady=5)

        # Relative Error Label
        relative_error_label = ttk.Label(self.root, text="Relative Error:")
        relative_error_value_label = ttk.Label(self.root, textvariable=self.relative_error_var)
        relative_error_label.grid(row=4, column=0, pady=5)
        relative_error_value_label.grid(row=4, column=1, pady=5)

        # Absolute Error Label
        absolute_error_label = ttk.Label(self.root, text="Absolute Error:")
        absolute_error_value_label = ttk.Label(self.root, textvariable=self.absolute_error_var)
        absolute_error_label.grid(row=5, column=0, pady=5)
        absolute_error_value_label.grid(row=5, column=1, pady=5)

        # Matplotlib Figure for Plot
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().grid(row=0, column=2, rowspan=6, padx=10)

    def solve_taylor_series(self):
        try:
            x = float(self.x_value.get())
            n = int(self.n_value.get())

            # Taylor series calculation
            taylor_series = sp.summation(sp.diff(sp.acos(self.term), self.term).subs(self.term, 0) / sp.factorial(self.i) * (x**self.i), (self.i, 0, n))

            # Display the result
            result = sp.N(taylor_series)
            self.result_var.set(result)

            # Plot the Taylor series
            self.plot_taylor_series(x, n)

            # Calculate and display errors
            actual_value = np.arccos(x) if -1 <= x <= 1 else np.nan
            relative_error = abs((actual_value - result) / actual_value) if not np.isnan(actual_value) else np.nan
            absolute_error = abs(actual_value - result) if not np.isnan(actual_value) else np.nan
            self.relative_error_var.set(f"{relative_error:.8f}" if not np.isnan(relative_error) else "NaN")
            self.absolute_error_var.set(f"{absolute_error:.8f}" if not np.isnan(absolute_error) else "NaN")

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numerical values.")

    def plot_taylor_series(self, x, n):
        self.ax.clear()
        x_vals = np.linspace(-1, 1, 100)
        y_vals = np.array([sp.N(sp.summation(sp.diff(sp.acos(self.term), self.term).subs(self.term, 0) / sp.factorial(self.i) * (x**self.i), (self.i, 0, n))) for x in x_vals])
        self.ax.plot(x_vals, y_vals, label=f'Taylor Series (n={n})')
        if not np.isnan(x):
            self.ax.axhline(y=np.arccos(x), color='r', linestyle='--', label='Actual Value')
        self.ax.legend()
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaylorSeriesSolverApp(root)
    root.mainloop()
