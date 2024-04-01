from sympy import symbols, Eq, solve

def solve_power_equation(a: float, b: float) -> str:
  """
  Solves a power equation of the form x^a = b.
  Returns the solutions x, or a string indicating that there are no solutions.

  Parameters:
  a (float): The exponent.
  b (float): The constant term.

  Returns:
  str: The solutions to the equation, or a string indicating that there are no solutions.
  """
  x = symbols('x')
  equation = Eq(x**a, b)
  solutions = solve(equation, x)
  
  if not solutions:
    return "No solution"
  else:
    return ', '.join(str(sol.evalf()) for sol in solutions)

# Example usage
a = 2.0
b = 4.0
solution = solve_power_equation(a, b)
print("Solution:", solution)