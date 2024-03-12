import tkinter as tk
from tkinter import Label, Entry, Button, messagebox, Toplevel
import sympy as sp

def compute_derivative(n, x_value):
    try:
        x = float(x_value)
        if -1 < x < 1:
            symbol_x = sp.symbols('x')
            expr = sp.acos(symbol_x)
            derivative_result = sp.diff(expr, symbol_x, n)
            result = derivative_result.subs(symbol_x, x)
            return result.evalf()
        else:
            messagebox.showerror("Input Error", "Invalid 'x' value. Please enter a value in the range -1 < x < 1.")
            return None
    except ValueError:
        messagebox.showerror("Input Error", "Invalid input. Please enter a valid floating-point number for 'x'.")
        return None

def taylor_polynomial(n, x):
    symbol_x = sp.symbols('x')
    expr = sp.acos(symbol_x)
    taylor_poly = sp.series(expr, symbol_x, 0, n).removeO()
    result = taylor_poly.subs(symbol_x, x)
    return result.evalf()

def calculate_and_display():
    n = int(degree_entry.get())
    x_value = x_entry.get()

    result = compute_derivative(n, x_value)
    if result is not None:
        result_label.config(text=f"Result: {result}")

def open_taylor_window():
    taylor_window = Toplevel(app)
    taylor_window.title("Taylor's Polynomial Representation")

    Label(taylor_window, text="Enter the degree (n):").pack(pady=5)
    degree_entry_taylor = Entry(taylor_window)
    degree_entry_taylor.pack(pady=5)

    def calculate_taylor_polynomial():
        n_taylor = int(degree_entry_taylor.get())
        try:
            taylor_result = taylor_polynomial(n_taylor )
            result_taylor_label.config(text=f"Taylor Polynomial Result: {taylor_result}")
        except ValueError:
            messagebox.showerror("Input Error", "Invalid input. Please enter a valid floating-point number for 'n'.")

    calculate_taylor_button = Button(taylor_window, text="Calculate Taylor Polynomial", command=calculate_taylor_polynomial)
    calculate_taylor_button.pack(pady=10)

    result_taylor_label = Label(taylor_window, text="")
    result_taylor_label.pack(pady=10)

# Create the main window
app = tk.Tk()
app.title("Arccos Derivative Calculator")

# Create and place widgets
Label(app, text="Enter the degree (n):").pack(pady=5)
degree_entry = Entry(app)
degree_entry.pack(pady=5)

Label(app, text="Enter the value of x (-1 < x < 1):").pack(pady=5)
x_entry = Entry(app)
x_entry.pack(pady=5)

calculate_button = Button(app, text="Calculate Derivative", command=calculate_and_display)
calculate_button.pack(pady=10)

result_label = Label(app, text="")
result_label.pack(pady=10)

taylor_button = Button(app, text="Open Taylor's Polynomial Window", command=open_taylor_window)
taylor_button.pack(pady=10)

# Run the application
app.mainloop()
