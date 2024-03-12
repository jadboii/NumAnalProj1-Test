import tkinter as tk
from tkinter import ttk
import sympy as sp


class NumberProcessor:
    def __init__(self, x, n):
        self.x = x
        self.n = n

    def validate_input(self):
        return -1 < self.x < 1 and isinstance(self.x, float) and isinstance(self.n, int)

    def calculate_higher_derivative_arccos(self):
        if self.validate_input():
            x_sym = sp.symbols('x')
            arccos_expr = sp.acos(x_sym)
            higher_derivative = sp.diff(arccos_expr, x_sym, self.n)
            result = higher_derivative.evalf(subs={x_sym: self.x})
            return result
        else:
            return None

    def calculate_taylor_polynomial(self):
        x_sym = sp.symbols('x')
        arccos_expr = sp.acos(x_sym)

        taylor_poly = arccos_expr.evalf(subs={x_sym: self.x})
        factorial_value = 1

        for i in range(1, self.n + 1):
            derivative = sp.diff(arccos_expr, x_sym, i)
            factorial_value *= i
            taylor_poly += (derivative.evalf(subs={x_sym: self.x}) / factorial_value) * (x_sym - self.x) ** factorial_value

        return taylor_poly

class NumberProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Higher Derivatives of arccos(x) Calculator")

        self.label_x = ttk.Label(root, text="Enter a value for x (-1 < x < 1):")
        self.label_x.pack(pady=5)

        self.entry_x = ttk.Entry(root)
        self.entry_x.pack(pady=5)

        self.label_n = ttk.Label(root, text="Enter the order of the derivative (n):")
        self.label_n.pack(pady=5)

        self.entry_n = ttk.Entry(root)
        self.entry_n.pack(pady=5)

        self.process_button = ttk.Button(root, text="Calculate Derivative", command=self.calculate_derivative)
        self.process_button.pack(pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.pack(pady=10)

    def calculate_derivative(self):
        user_input_x = self.entry_x.get()
        user_input_n = self.entry_n.get()

        try:
            x_value = float(user_input_x)
            n_value = int(user_input_n)

            processor = NumberProcessor(x_value, n_value)
            result = processor.calculate_higher_derivative_arccos()

            if result is not None:
                result_text = f"The {n_value}-th derivative of arccos({x_value}) is: {result}"
                self.result_label.config(text=result_text)

                # Open a new window for 'c'
                new_window_c = tk.Toplevel(self.root)
                new_window_c.title("New Window for c")

                c_label = ttk.Label(new_window_c, text="Enter a value for c:")
                c_label.pack(pady=5)

                entry_c = ttk.Entry(new_window_c)
                entry_c.pack(pady=5)

                multiply_button = ttk.Button(new_window_c, text="Multiply and Display", command=lambda: self.multiply_and_display(entry_c, result))
                multiply_button.pack(pady=10)
            else:
                self.result_label.config(text="Invalid input. Please ensure -1 < x < 1 and provide valid values.")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter valid numerical values.")

    def multiply_and_display(self, entry_c, result):
        try:
            c_value = float(entry_c.get())
            updated_result = result * c_value
            result_text = f"The updated result after multiplying by {c_value} is: {updated_result}"
            self.result_label.config(text=result_text)

            # Open a new window for 'n'
            new_window_n = tk.Toplevel(self.root)
            new_window_n.title("New Window for n")

            n_label = ttk.Label(new_window_n, text="Enter the degree of the Taylor polynomial (n):")
            n_label.pack(pady=5)

            entry_n_taylor = ttk.Entry(new_window_n)
            entry_n_taylor.pack(pady=5)

            calculate_taylor_button = ttk.Button(new_window_n, text="Calculate Taylor Polynomial", command=lambda: self.calculate_taylor(entry_n_taylor, updated_result))
            calculate_taylor_button.pack(pady=10)
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a valid numerical value for 'c'.")

    def calculate_taylor(self, entry_n_taylor, updated_result):
        try:
            n_taylor_value = int(entry_n_taylor.get())
            processor = NumberProcessor(updated_result, n_taylor_value)
            taylor_polynomial = processor.calculate_taylor_polynomial()
            result_text = f"The Taylor Polynomial of degree {n_taylor_value} is: {taylor_polynomial}"
            self.result_label.config(text=result_text)
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a valid numerical value for 'n'.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberProcessorApp(root)
    root.mainloop()

