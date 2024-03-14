import sympy as sp
import math
import tkinter as tk
from tkinter import Label, Entry, Button, StringVar

def calculate_arccos(x):
    if -1 <= x <= 1:
        return math.acos(x)
    else:
        return "Error: Input value must be between -1 and 1"

def taylor_series_arccos(x, c, n):
    x_sym = sp.Symbol('x')
    c_sym = sp.Symbol('c')
    func = sp.acos(x_sym)
    derivatives = [func.diff(x_sym, i) for i in range(n + 1)]
    series = sum(derivatives[i].subs(x_sym, c_sym) * (x_sym - c_sym)**i / sp.factorial(i)
                 for i in range(n + 1))
    approx = series.subs([(x_sym, x), (c_sym, c)])
    return approx

def truncate_decimal(number, decimal_places):
    power_of_ten = 10 ** decimal_places
    truncated_number = int(number * power_of_ten) / power_of_ten
    return truncated_number

def calculate_approximation():
    x = float(entry_x.get())
    c = float(entry_c.get())
    n = int(entry_n.get())
    d = int(entry_d.get())

    user_choice = rounding_chopping_var.get()

    taylor_series_approx = taylor_series_arccos(x, c, n)
    absolute_value = calculate_arccos(x)

    if user_choice == "rounding":
        estimated_value = round(taylor_series_approx, d)
        choiceU = "Rounding"
        if d == 0:
            estimated_value = taylor_series_approx  # No rounding
        else:
            estimated_value = round(taylor_series_approx, d)

    elif user_choice == "chopping":
        estimated_value = truncate_decimal(taylor_series_approx, d)
        choiceU = "Chopping"  # Fix the variable name here
        if d == 0:
            estimated_value = taylor_series_approx  # No chopping
        else:
            estimated_value = truncate_decimal(taylor_series_approx, d)

    absolute_error = (absolute_value - estimated_value)
    relative_error = (absolute_error / absolute_value) * 100

    result_text.set(f"True Value: {absolute_value}\n"
                    f"Taylor Series Approx: {taylor_series_approx}\n"
                    f"Estimated Value ({choiceU}): {estimated_value}\n"
                    f"Absolute Error: {abs(absolute_error)}%\n"
                    f"Relative Error: {abs(relative_error)}%")

# Create Tkinter window
window = tk.Tk()
window.title("Arccosine Approximation")

# Create input fields
Label(window, text="Enter the value of x:").pack()
entry_x = Entry(window)
entry_x.pack()

Label(window, text="Enter the center point (c):").pack()
entry_c = Entry(window)
entry_c.pack()

Label(window, text="Enter the order of the derivative (n):").pack()
entry_n = Entry(window)
entry_n.pack()

Label(window, text="Enter the number of decimals for approx value:").pack()
entry_d = Entry(window)
entry_d.pack()

# Create radio buttons for rounding/chopping
rounding_chopping_var = StringVar()
rounding_chopping_var.set("rounding")
rounding_button = tk.Radiobutton(window, text="Rounding", variable=rounding_chopping_var, value="rounding")
rounding_button.pack()
chopping_button = tk.Radiobutton(window, text="Chopping", variable=rounding_chopping_var, value="chopping")
chopping_button.pack()

# Create calculate button
calculate_button = Button(window, text="Calculate", command=calculate_approximation)
calculate_button.pack()

# Create result label
result_text = StringVar()
result_label = Label(window, textvariable=result_text)
result_label.pack()

# Start the Tkinter event loop
window.mainloop()
