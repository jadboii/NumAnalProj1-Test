import tkinter as tk
from sympy import symbols, diff, acos, N, factorial

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

def calculate_taylor_polynomial(higher_derivative_order, deg):
    x = symbols('x')
    taylor_poly_coefficients = [higher_derivative_order.subs(x, 0) / factorial(i) for i in range(deg + 1)]
    taylor_poly = sum(c * x**i for i, c in enumerate(taylor_poly_coefficients))
    return N(taylor_poly)

def on_calculate():
    try:
        c_value = float(entry_c.get())
        n_value = int(entry_n.get())
        true_val = float(entry_true_val.get())

        # Input validation
        if not (-1 < c_value < 1) or n_value < 0:
            raise ValueError("Invalid input values.")

        higher_derivative_result = calculate_higher_derivative(c_value, n_value)
        true_value_result = calculate_true_value(true_val)

        result_label.config(text=f"Higher Derivative: {higher_derivative_result}\nTrue Value: {true_value_result}")

        # Create a new dialog for Taylor polynomial calculation
        taylor_dialog = tk.Toplevel(root)
        taylor_dialog.title("Taylor Polynomial Calculator")

        # Ask the user for the degree of Taylor polynomial
        label_deg = tk.Label(taylor_dialog, text="Enter the degree for Taylor polynomial:")
        label_deg.pack()

        entry_deg = tk.Entry(taylor_dialog)
        entry_deg.pack()

        def calculate_taylor():
            try:
                deg_value = int(entry_deg.get())
                taylor_poly_answer = calculate_taylor_polynomial(higher_derivative_result, deg_value)
                taylor_result_label.config(text=f"Taylor Polynomial: {taylor_poly_answer}")

            except ValueError:
                taylor_result_label.config(text="Invalid degree input.")

        calculate_taylor_button = tk.Button(taylor_dialog, text="Calculate Taylor Polynomial", command=calculate_taylor)
        calculate_taylor_button.pack()

        taylor_result_label = tk.Label(taylor_dialog, text="")
        taylor_result_label.pack()

    except ValueError as e:
        result_label.config(text=f"Error: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Arccos(x) Derivative Calculator")

# Create and place widgets with better spacing
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
