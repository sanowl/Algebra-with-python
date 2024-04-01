from sympy import symbols, Eq, solve, sec

def solve_secant_equation(a: float, b: float, c: float) -> str:
  """
  Solves a secant equation of the form sec(ax + b) = c.
  Returns the solutions x, or a string indicating that there are no solutions.

  Parameters:
  a (float): The coefficient of x inside the secant function.
  b (float): The constant term inside the secant function.
  c (float): The constant term on the right side of the equation.

  Returns:
  str: The solutions to the equation, or a string indicating that there are no solutions.
  """
  x = symbols('x')
  equation = Eq(sec(a*x + b), c)
  solutions = solve(equation, x)
  
  if not solutions:
    return "No solution"
  else:
    return ', '.join(str(sol.evalf()) for sol in solutions)

# Example usage
a = 2.0
b = 3.0
c = 4.0
solution = solve_secant_equation(a, b, c)
print("Solution:", solution)