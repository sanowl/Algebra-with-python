import  math


def solve_trigonometric_equation(a: float, b: float) -> float:
    """
    Solves a trigonometric equation of the form sin(ax) = b.
    Returns the solution x in radians.

    Parameters:
    a (float): The coefficient of x inside the sine function.
    b (float): The constant term on the right side of the equation.

    Returns:
    float: The solution to the equation in radians.
    """
    # Use the arcsin function to solve for x
    x = math.asin(b) / a
    return x

if __name__ == "__main__":
    a = 2.0
    b = 0.5
    solution = solve_trigonometric_equation(a, b)
    print("Solution:", solution)