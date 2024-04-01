from sympy import symbols, cosh, solve

def solve_hyperbolic_equation(a: float, b: float) -> str:
  """
  Solves a hyperbolic equation of the form a * cosh(x) + b = 0.
  Returns the solution x, or a string indicating that there are no solutions.

  Parameters:
  a (float): The coefficient of cosh(x).
  b (float): The constant term.

  Returns:
  str: The solution to the equation, or a string indicating that there are no solutions.
  """
  x = symbols('x')
  equation = a * cosh(x) + b
  solutions = solve(equation, x)
  
  if not solutions:
    return "No solution"
  else:
    return ', '.join(str(sol.evalf()) for sol in solutions)

# Example usage
a = 2.0
b = -1.0
solution = solve_hyperbolic_equation(a, b)
print("Solution:", solution)