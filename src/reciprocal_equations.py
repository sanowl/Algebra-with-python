from typing import Union

def solve_reciprocal_equation(coeff_x: float, const_term: float, right_side: float) -> Union[str, float]:
    """
    Solves a reciprocal equation of the form 1/(ax + b) = c.
    Returns the solution x as a float, or a string indicating that there are no solutions or the inputs are invalid.

    Parameters:
    coeff_x (float): The coefficient of x in the denominator.
    const_term (float): The constant term in the denominator.
    right_side (float): The constant term on the right side of the equation.

    Returns:
    Union[str, float]: The solution to the equation as a float, or a string indicating that there are no solutions or the inputs are invalid.
    """
    # Check for invalid inputs
    if coeff_x == 0 and const_term == 0:
        raise ValueError("Invalid inputs: Denominator cannot be zero.")
    if right_side == 0:
        raise ValueError("Invalid inputs: Right side of the equation cannot be zero.")

    # Handle special case when coeff_x is zero
    if coeff_x == 0:
        if const_term != 0 and 1 / const_term == right_side:
            return "The equation has infinitely many solutions. Any value of x is a solution."
        else:
            return "The equation has no solution."

    # Cross-multiply to get rid of the fraction
    numerator = 1 - const_term * right_side
    denominator = coeff_x * right_side

    # Check if the solution is valid
    if denominator == 0:
        return "The equation has no solution."
    else:
        solution = numerator / denominator
        return solution

def main():
    # Get user input for the coefficients and right side of the equation
    coeff_x = float(input("Enter the coefficient of x in the denominator: "))
    const_term = float(input("Enter the constant term in the denominator: "))
    right_side = float(input("Enter the constant term on the right side of the equation: "))

    try:
        solution = solve_reciprocal_equation(coeff_x, const_term, right_side)
        if isinstance(solution, str):
            print(solution)
        else:
            print(f"The solution to the equation is: x = {solution:.2f}")
    except ValueError as e:
        print(str(e))

if __name__ == "__main__":
    main()