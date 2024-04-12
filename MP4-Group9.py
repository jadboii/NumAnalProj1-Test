import tkinter as tk
import sympy as sp

def open_fraction_polynomial_window():
    fraction_polynomial_window = tk.Toplevel(root)
    fraction_polynomial_window.title("Fraction Polynomial")

    # Numerator entry
    numerator_label = tk.Label(fraction_polynomial_window, text="Numerator:")
    numerator_label.grid(row=0, column=0, sticky="w")
    numerator_entry = tk.Entry(fraction_polynomial_window)
    numerator_entry.grid(row=0, column=1, sticky="w")

    # Denominator entry
    denominator_label = tk.Label(fraction_polynomial_window, text="Denominator:")
    denominator_label.grid(row=1, column=0, sticky="w")
    denominator_entry = tk.Entry(fraction_polynomial_window)
    denominator_entry.grid(row=1, column=1, sticky="w")

    def return_values():
        numerator = numerator_entry.get()
        denominator = denominator_entry.get()
        polynomial_str = f"({numerator})/({denominator})"
        polynomial_entry.delete(0, tk.END)
        polynomial_entry.insert(0, polynomial_str)
        fraction_polynomial_window.destroy()

    return_button = tk.Button(fraction_polynomial_window, text="Return", command=return_values)
    return_button.grid(row=2, columnspan=2, pady=10)


def calculate():
    polynomial_str = polynomial_entry.get()
    x_val = float(x_val_entry.get())
    epsilon_error = float(epsilon_entry.get())

    x = sp.Symbol('x')
    polynomial = sp.sympify(polynomial_str)
    derivative = sp.diff(polynomial, x)
    poly_solve = polynomial.subs(x, x_val)
    derivative_solve = derivative.subs(x, x_val)
    iterate_x = x_val - (poly_solve / derivative_solve)
    epsilon = abs(iterate_x - x_val)

    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"Initial Value (x): {x_val}\n")
    result_text.insert(tk.END, f"Error: {epsilon_error}\n\n")
    result_text.insert(tk.END, f"n=1\n")
    result_text.insert(tk.END, f"xn: {x_val}\n")
    result_text.insert(tk.END, f"f'(x): {derivative}\n")
    result_text.insert(tk.END, f"f(xn): {poly_solve}\n")
    result_text.insert(tk.END, f"f'(xn): {derivative_solve}\n")
    result_text.insert(tk.END, f"xn+1: {iterate_x}\n")
    result_text.insert(tk.END, f"|xn+1 - xn|: {epsilon}\n\n")

    n = 1
    while epsilon >= epsilon_error:
        n += 1
        x_val = iterate_x
        poly_solve = polynomial.subs(x, x_val)
        derivative_solve = derivative.subs(x, x_val)
        iterate_x = x_val - (poly_solve / derivative_solve)
        epsilon = abs(iterate_x - x_val)
        result_text.insert(tk.END, f"n={n}\n")
        result_text.insert(tk.END, f"xn: {x_val}\n")
        result_text.insert(tk.END, f"f'(x): {derivative}\n")
        result_text.insert(tk.END, f"f(xn): {poly_solve}\n")
        result_text.insert(tk.END, f"f'(xn): {derivative_solve}\n")
        result_text.insert(tk.END, f"xn+1: {iterate_x}\n")
        result_text.insert(tk.END, f"|xn+1 - xn|: {epsilon}\n\n")

    result_text.config(state=tk.DISABLED)


# Create main window
root = tk.Tk()
root.title("Newton-Raphson Method")

# Polynomial entry
polynomial_label = tk.Label(root, text="Enter your polynomial:")
polynomial_label.grid(row=0, column=0, sticky="w")
polynomial_entry = tk.Entry(root, width=50)
polynomial_entry.grid(row=0, column=1, columnspan=2)

# Fraction Polynomial button
fraction_button = tk.Button(root, text="Fraction Polynomial", command=open_fraction_polynomial_window)
fraction_button.grid(row=0, column=3, padx=10)

# Initial value entry
x_val_label = tk.Label(root, text="Enter initial value:")
x_val_label.grid(row=1, column=0, sticky="w")
x_val_entry = tk.Entry(root)
x_val_entry.grid(row=1, column=1, sticky="w")

# Error entry
epsilon_label = tk.Label(root, text="Enter error or accuracy value:")
epsilon_label.grid(row=2, column=0, sticky="w")
epsilon_entry = tk.Entry(root)
epsilon_entry.grid(row=2, column=1, sticky="w")

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=1, pady=10)

# Result text
result_text = tk.Text(root, height=20, width=70)
result_text.grid(row=4, column=0, columnspan=4, padx=10, pady=10)
result_text.config(state=tk.DISABLED)

root.mainloop()
