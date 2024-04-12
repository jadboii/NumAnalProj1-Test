import sympy as sp

class BisectionMethod:
    def __init__(self, a, b, function_inp, epsilon_error):
        self.a = a
        self.b = b
        self.x = sp.Symbol('x')
        self.function = sp.sympify(function_inp)
        self.epsilon_error = epsilon_error
        self.n = 1

    def calculate(self):
        self.c = (self.a + self.b) / 2
        self.epsilon = self.b - self.a

        while self.epsilon > self.epsilon_error:
            self.f_a = self.function.subs(self.x, self.a)
            self.f_b = self.function.subs(self.x, self.b)
            self.f_c = self.function.subs(self.x, self.c)

            self.print_values()

            if self.f_c > 0:
                self.b = self.c
            elif self.f_c < 0:
                self.a = self.c

            self.c = (self.a + self.b) / 2
            self.epsilon = self.b - self.a
            self.n += 1

    def print_values(self):
        print(f'\nn = {self.n}\n')
        print(f'f(a): {self.f_a}')
        print(f'f(b): {self.f_b}')
        print(f'C: {self.c}')
        print(f'f(c): {self.f_c}')
        print(f'b-a: {self.epsilon}')


# Taking user input for a, b, and the function
a = float(input('Enter value of a: '))
b = float(input('Enter value of b: '))
function_inp = input('Enter function: ')
epsilon_error = float(input('Enter epsilon error value: '))

# Create an instance of BisectionMethod and perform the calculation
bisection_method = BisectionMethod(a, b, function_inp, epsilon_error)
bisection_method.calculate()