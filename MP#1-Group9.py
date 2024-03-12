import tkinter as tk
from tkinter import ttk, simpledialog
import sympy as sp

class NumberProcessor:
    def __init__(self, number):
        self.number = number

    def chop_number(self, decimal_points):
        factor = 10 ** decimal_points
        chopped_number = int(self.number * factor) / factor
        return chopped_number

    def round_number(self, decimal_points):
        rounded_number = round(self.number, decimal_points)
        return rounded_number

    def calculate_absolute_error(self, true_value, estimated_value):
        return (abs(true_value - estimated_value))*10

    def calculate_relative_error(self, absolute_error, estimated_value):
        return (absolute_error / abs(estimated_value))*10

    def calculate_fraction(self, numerator, denominator):
        try:
            fraction_result = sp.Rational(numerator, denominator)
            return float(fraction_result)
        except ZeroDivisionError:
            return None  # Handle division by zero eror

    def calculate_square_root(self):
        if self.number >= 0:
            return sp.sqrt(self.number)
        else:
            return None  # Handle square root of negative number

class NumberProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Machine Problem #1 - Group 9")

        self.label = ttk.Label(root, text="Enter a float number:")
        self.label.pack(pady=10)

        self.user_input_var = tk.StringVar()
        self.entry = ttk.Entry(root, textvariable=self.user_input_var)
        self.entry.pack(pady=10)

        self.decimal_label = ttk.Label(root, text="Enter decimal points:")
        self.decimal_label.pack(pady=5)

        self.decimal_entry_var = tk.StringVar()
        self.decimal_entry = ttk.Entry(root, textvariable=self.decimal_entry_var)
        self.decimal_entry.pack(pady=5)

        self.process_button = ttk.Button(root, text="Process", command=self.process_number)
        self.process_button.pack(pady=10)

        self.fraction_button = ttk.Button(root, text="Fraction Input", command=self.get_fraction_input)
        self.fraction_button.pack(pady=10)

        self.sqrt_button = ttk.Button(root, text="Square Root Input", command=self.get_square_root_input)
        self.sqrt_button.pack(pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.pack(pady=10)

    def process_number(self):
        user_input = self.user_input_var.get()

        try:
            user_number = float(user_input)
            decimal_points = int(self.decimal_entry_var.get())

            processor = NumberProcessor(user_number)
            chopped_result = processor.chop_number(decimal_points)
            rounded_result = processor.round_number(decimal_points)

            absolute_error_chop = processor.calculate_absolute_error(user_number, chopped_result)
            relative_error_chop = processor.calculate_relative_error(absolute_error_chop, chopped_result)

            absolute_error_round = processor.calculate_absolute_error(user_number, rounded_result)
            relative_error_round = processor.calculate_relative_error(absolute_error_round, rounded_result)

            result_text = f"Original Number: {user_number}\n"
            result_text += f"Chopped Number: {chopped_result}\n"
            result_text += f"Rounded Number: {rounded_result}\n\n"

            result_text += f"Absolute Error (Chopping): {absolute_error_chop}%\n"
            result_text += f"Relative Error (Chopping): {relative_error_chop}%\n\n"

            result_text += f"Absolute Error (Rounding): {absolute_error_round}%\n"
            result_text += f"Relative Error (Rounding): {relative_error_round}%"

            self.result_label.config(text=result_text)
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a valid float number.")

    def get_fraction_input(self):
        numerator = simpledialog.askfloat("Fraction Input", "Enter numerator:")
        denominator = simpledialog.askfloat("Fraction Input", "Enter denominator:")
        if numerator is not None and denominator is not None:
            processor = NumberProcessor(self.user_input_var.get())
            fraction_result = processor.calculate_fraction(numerator, denominator)
            if fraction_result is not None:
                self.user_input_var.set(str(fraction_result))
            else:
                self.result_label.config(text="Error: Division by zero")

    def get_square_root_input(self):
        user_input = simpledialog.askfloat("Square Root Input", "Enter a value:")
        if user_input is not None and user_input >= 0:
            processor = NumberProcessor(user_input)
            sqrt_result = processor.calculate_square_root()
            if sqrt_result is not None:
                self.user_input_var.set(sqrt_result)
            else:
                self.result_label.config(text="Error: Cannot calculate square root of a negative number")


if __name__ == "__main__":
    root = tk.Tk()
    app = NumberProcessorApp(root)
    root.mainloop()
