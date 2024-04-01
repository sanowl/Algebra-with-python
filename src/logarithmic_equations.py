from sympy import symbols, log, solve

def solve_logarithmic_equation(a: float, b: float, base: float) -> str:
  """
  Solves a logarithmic equation of the form a * log(x, base) + b = 0.
  Returns the solution x, or a string indicating that there are no solutions.

  Parameters:
  a (float): The coefficient of log(x, base).
  b (float): The constant term.
  base (float): The base of the logarithm.

  Returns:
  str: The solution to the equation, or a string indicating that there are no solutions.
  """
  x = symbols('x')
  equation = a * log(x, base) + b
  solutions = solve(equation, x)
  
  if not solutions:
    return "No solution"
  else:
    return ', '.join(str(sol.evalf()) for sol in solutions)

# Example usage
a = 2.0
b = -1.0
base = 10.0
solution = solve_logarithmic_equation(a, b, base)
print("Solution:", solution)