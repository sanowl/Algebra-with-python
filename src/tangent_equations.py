from sympy import symbols, Eq, solve, tan

def solve_tangent_equation(a: float, b: float, c: float) -> str:
  """
  Solves a tangent equation of the form tan(ax + b) = c.
  Returns the solutions x, or a string indicating that there are no solutions.

  Parameters:
  a (float): The coefficient of x inside the tangent function.
  b (float): The constant term inside the tangent function.
  c (float): The constant term on the right side of the equation.

  Returns:
  str: The solutions to the equation, or a string indicating that there are no solutions.
  """
  x = symbols('x')
  equation = Eq(tan(a*x + b), c)
  solutions = solve(equation, x)
  
  if not solutions:
    return "No solution"
  else:
    return ', '.join(str(sol.evalf()) for sol in solutions)

# Example usage
a = 2.0
b = 3.0
c = 1.0
solution = solve_tangent_equation(a, b, c)
print("Solution:", solution)