from sympy import symbols, Eq, solve

def solve_quartic_equation(a: float, b: float, c: float, d: float, e: float) -> str:
  """
  Solves a quartic equation of the form ax^4 + bx^3 + cx^2 + dx + e = 0.
  Returns the solutions x, or a string indicating that there are no solutions.

  Parameters:
  a (float): The coefficient of x^4.
  b (float): The coefficient of x^3.
  c (float): The coefficient of x^2.
  d (float): The coefficient of x.
  e (float): The constant term.

  Returns:
  str: The solutions to the equation, or a string indicating that there are no solutions.
  """
  x = symbols('x')
  equation = Eq(a*x**4 + b*x**3 + c*x**2 + d*x + e, 0)
  solutions = solve(equation, x)
  
  if not solutions:
    return "No solution"
  else:
    return ', '.join(str(sol.evalf()) for sol in solutions)

# Example usage
a = 1.0
b = -10.0
c = 35.0
d = -50.0
e = 24.0
solution = solve_quartic_equation(a, b, c, d, e)
print("Solution:", solution)