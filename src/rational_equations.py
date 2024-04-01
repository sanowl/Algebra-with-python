from sympy import symbols, Eq, solve

def solve_rational_equation(a: float, b: float, c: float, d: float, e: float) -> str:
  """
  Solves a rational equation of the form (ax + b) / (cx + d) = e.
  Returns the solutions x, or a string indicating that there are no solutions.

  Parameters:
  a (float): The coefficient of x in the numerator.
  b (float): The constant term in the numerator.
  c (float): The coefficient of x in the denominator.
  d (float): The constant term in the denominator.
  e (float): The constant term on the right side of the equation.

  Returns:
  str: The solutions to the equation, or a string indicating that there are no solutions.
  """
  x = symbols('x')
  equation = Eq((a*x + b) / (c*x + d), e)
  solutions = solve(equation, x)
  
  if not solutions:
    return "No solution"
  else:
    return ', '.join(str(sol.evalf()) for sol in solutions)

# Example usage
a = 1.0
b = -2.0
c = 3.0
d = -4.0
e = 2.0
solution = solve_rational_equation(a, b, c, d, e)
print("Solution:", solution)