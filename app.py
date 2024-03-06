import numpy as np
import scipy as sp
import sympy as smp
from sympy import symbols, diff, exp, factorial, pretty, pretty_print
import matplotlib.pyplot as plt
from scipy.misc import derivative
from tkinter import *

x = smp.symbols('x', real=True)
equation = smp.acos(x)

root = Tk()
root.title("Taylor's polynomial - Group 9")
root.geometry('500x500')

Header = Label(root, text='ASSIGNED FUNCTION: ', font=('Georgia', 25, 'bold'), justify='center')
Header.place(x=55, y=30)

myLabel = Label(root, text=f'{equation}', font=('Georgia', 25, 'italic'), justify='center')
myLabel.place(x=200, y=80)

myLabel1 = Label(root, text='Enter no. of degrees: ', font=('Georgia', 10), justify='center')
myLabel1.place(x=200, y=80)

e = Entry(root, width=30)

myLabel2 = Label(root, text='Enter x value: ', font=('Georgia', 10), justify='center')
myLabel2.place(x=200, y=80)

e2 = Entry(root, width=30)
def solve():
    func = equation
    n = int(e.get())
    x = int(e2.get())
    res = func.subs(x, x0)

    for i in range(1, n):
        res += diff(func, x, i).subs(x, x0)*(x - x0) ** i / factorial(i)

    ans = pretty_print(res, use_unicode=True)
    answer.config(text=f'Answer: \n \n {ans}')


b = Button(root, text="Enter", command=solve)

answer = Label(root, text='', font=('Georgia', 10), justify='center')

Header.place(x=55, y=30)
Header.pack()
myLabel.pack()
myLabel1.pack()
e.pack(pady=5)
myLabel2.pack()
e2.pack(pady=5)
b.pack(pady=5)
answer.pack(pady=5)

root.mainloop()