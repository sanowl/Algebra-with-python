from sympy import symbols, Eq, solve, sqrt

def solve_radical_equation(a: float, b: float, c: float) -> str:
  """
  Solves a radical equation of the form sqrt(ax + b) = c.
  Returns the solutions x, or a string indicating that there are no solutions.

  Parameters:
  a (float): The coefficient of x inside the square root.
  b (float): The constant term inside the square root.
  c (float): The constant term on the right side of the equation.

  Returns:
  str: The solutions to the equation, or a string indicating that there are no solutions.
  """
  x = symbols('x')
  equation = Eq(sqrt(a*x + b), c)
  solutions = solve(equation, x)
  
  if not solutions:
    return "No solution"
  else:
    return ', '.join(str(sol.evalf()) for sol in solutions)

# Example usage
a = 2.0
b = 3.0
c = 2.0
solution = solve_radical_equation(a, b, c)
print("Solution:", solution)