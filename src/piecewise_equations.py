from sympy import symbols, Piecewise, solve

def solve_piecewise_equation(a: float, b: float, c: float, d: float) -> str:
  """
  Solves a piecewise equation of the form ax + b for x < 0 and cx + d for x >= 0.
  Returns the solutions x, or a string indicating that there are no solutions.

  Parameters:
  a (float): The coefficient of x for x < 0.
  b (float): The constant term for x < 0.
  c (float): The coefficient of x for x >= 0.
  d (float): The constant term for x >= 0.

  Returns:
  str: The solutions to the equation, or a string indicating that there are no solutions.
  """
  x = symbols('x')
  equation = Piecewise((a*x + b, x < 0), (c*x + d, x >= 0))
  solutions = solve(equation, x)
  
  if not solutions:
    return "No solution"
  else:
    return ', '.join(str(sol.evalf()) for sol in solutions)

# Example usage
a = 2.0
b = -1.0
c = -1.0
d = 2.0
solution = solve_piecewise_equation(a, b, c, d)
print("Solution:", solution)