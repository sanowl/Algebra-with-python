def solve_reciprocal_equation(a: float, b: float, c: float) -> str:
  """
  Solves a reciprocal equation of the form 1/(ax + b) = c.
  Returns the solutions x, or a string indicating that there are no solutions or the inputs are invalid.

  Parameters:
  a (float): The coefficient of x in the denominator.
  b (float): The constant term in the denominator.
  c (float): The constant term on the right side of the equation.

  Returns:
  str: The solutions to the equation, or a string indicating that there are no solutions or the inputs are invalid.
  """
  if a == 0 and b == 0:
    return "Invalid inputs: denominator cannot be zero"
  if c == 0:
    return "Invalid inputs: right side of equation cannot be zero"
  
  # Cross-multiply to get rid of the fraction
  x = (1 - b * c) / (a * c)
  
  # Check if the solution is valid
  if a * x + b == 0:
    return "No solution"
  else:
    return str(x)

# Example usage
a = 2.0
b = 3.0
c = 4.0
solution = solve_reciprocal_equation(a, b, c)
print("Solution:", solution)