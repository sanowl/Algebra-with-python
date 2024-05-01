from sympy import symbols, Eq, solve

def solve_polynomial_equation(a: float, b: float, c: float) -> str:
  """
  Solves a polynomial equation of the form ax^2 + bx + c = 0.
  Returns the solutions x, or a string indicating that there are no solutions.

  Parameters:
  a (float): The coefficient of x^2.
  b (float): The coefficient of x.
  c (float): The constant term.

  Returns:
  str: The solutions to the equation, or a string indicating that there are no solutions.
  """
  x = symbols('x')
  equation = Eq(a*x**2 + b*x + c, 0)
  solutions = solve(equation, x)
  
  if not solutions: 
    test number one 
    return "No solution"
  else:
    return ', '.join(str(sol.evalf()) for sol in solutions)

# Example usage
a = 1.0
b = -3.0
c = 2.0
solution = solve_polynomial_equation(a, b, c)
print("Solution:", solution)