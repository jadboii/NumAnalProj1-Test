import tkinter as tk
import sympy as sp


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
result_text.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
result_text.config(state=tk.DISABLED)

root.mainloop()
