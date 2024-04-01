"""
Linear algebra is a branch of mathematics that studies vectors, vector spaces (also called linear spaces), 
linear transformations (functions that preserve the operations of addition and scalar multiplication), 
and systems of linear equations. Linear equations themselves are equations of the first degree 
(meaning that the highest exponent of the variable is 1). In this file, we're specifically dealing 
with linear equations in one variable of the form ax + b = 0.
"""

import math

def solve_linear_equation(a: float, b: float) -> str:
  """
  Solves a linear equation of the form ax + b = 0.
  Returns the solution x, or a string indicating that there are no solutions or infinite solutions.

  Parameters:
  a (float): The coefficient of x.
  b (float): The constant term.

  Returns:
  str: The solution to the equation, or a string indicating that there are no solutions or infinite solutions.
  """
  if math.isclose(a, 0):
    if math.isclose(b, 0):
      return "Infinite solutions"
    else:
      return "No solution" 
  else:
    return str(-b / a)

# Example usage
a = 2.0
b = 4.0
solution = solve_linear_equation(a, b)
print("Solution:", solution)