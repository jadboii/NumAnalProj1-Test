import tkinter as tk
from tkinter import ttk
import sympy as sp
import numpy as np
from scipy.stats import truncnorm

class NumberProcessor:
    def __init__(self, x, n):
        self.x = x
        self.n = n

    def calculate_arccos_derivative(self):
        # Symbolic representation of arccos(x) and its derivatives
        symbol_x = sp.Symbol('x')
        arccos_expression = sp.acos(symbol_x)
        arccos_derivative = arccos_expression.diff(symbol_x, self.n)

        # Substitute user input 'x' into the expression
        user_number = arccos_derivative.subs(symbol_x, self.x).evalf()
        return user_number

    def chop_number(self, decimal_points, value):
        factor = 10 ** decimal_points
        chopped_value = int(value * factor) / factor
        return chopped_value

    def round_number(self, decimal_points, value):
        rounded_value = round(value, decimal_points)
        return rounded_value

    def calculate_absolute_error(self, true_value, estimated_value):
        return abs(true_value - estimated_value)

    def calculate_relative_error(self, absolute_error, estimated_value):
        return absolute_error / abs(estimated_value)

class NumberProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Taylor's")

        self.label_x = ttk.Label(root, text="Enter a value for x (-1 < x < 1):")
        self.label_x.pack(pady=5)

        self.entry_x = ttk.Entry(root)
        self.entry_x.pack(pady=5)

        self.label_n = ttk.Label(root, text="Enter the degree of the derivative (n):")
        self.label_n.pack(pady=5)

        self.entry_n = ttk.Entry(root)
        self.entry_n.pack(pady=5)

        self.decimal_label = ttk.Label(root, text="Enter decimal points:")
        self.decimal_label.pack(pady=5)

        self.decimal_entry = ttk.Entry(root)
        self.decimal_entry.pack(pady=5)

        self.process_button = ttk.Button(root, text="Process", command=self.process_number)
        self.process_button.pack(pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.pack(pady=10)

    def process_number(self):
        x_input = self.entry_x.get()
        n_input = self.entry_n.get()

        try:
            x_value = float(x_input)
            n_value = int(n_input)

            if -1 < x_value < 1:
                processor = NumberProcessor(x_value, n_value)

                user_number = processor.calculate_arccos_derivative()

                decimal_points = int(self.decimal_entry.get())

                chopped_result = processor.chop_number(decimal_points, user_number)
                rounded_result = processor.round_number(decimal_points, user_number)

                absolute_error_chop = processor.calculate_absolute_error(user_number, chopped_result)
                relative_error_chop = processor.calculate_relative_error(absolute_error_chop, chopped_result)

                absolute_error_round = processor.calculate_absolute_error(user_number, rounded_result)
                relative_error_round = processor.calculate_relative_error(absolute_error_round, rounded_result)

                result_text = f"Original Number (arccos({x_value})^{n_value}): {user_number}\n"
                result_text += f"Chopped Number: {chopped_result}\n"
                result_text += f"Rounded Number: {rounded_result}\n\n"

                result_text += f"Absolute Error (Chopping): {absolute_error_chop}\n"
                result_text += f"Relative Error (Chopping): {relative_error_chop}\n\n"

                result_text += f"Absolute Error (Rounding): {absolute_error_round}\n"
                result_text += f"Relative Error (Rounding): {relative_error_round}"

                self.result_label.config(text=result_text)
            else:
                self.result_label.config(text="Invalid input for 'x'. Please enter a value between -1 and 1.")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter valid values for 'x' and 'n'.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberProcessorApp(root)
    root.mainloop()
