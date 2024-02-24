# Problem finished by Austin
import numpy as np
from scipy.optimize import fsolve

def func1(x):
    """
    Function definition for the first function: x - 3cos(x)

    Parameters:
    x (float or array_like): Input value(s) for which the function value is calculated.

    Returns:
    float or array_like: Value(s) of the function at the input value(s) x.
    """
    return x - 3 * np.cos(x)

def func2(x):
    """
    Function definition for the second function: cos(2x) * x^3

    Parameters:
    x (float or array_like): Input value(s) for which the function value is calculated.

    Returns:
    float or array_like: Value(s) of the function at the input value(s) x.
    """
    return np.cos(2*x) * (x ** 3)

# Use fsolve to find the roots of the first function
roots_func1 = fsolve(func1, [-5, 5])

# Use fsolve to find the roots of the second function
roots_func2 = fsolve(func2, [-5, 5])

# Check if there are any intersections
intersection_points = [root for root in roots_func1 if root in roots_func2]

# Print the roots of the first function
print("Roots of x - 3cos(x) = 0:", roots_func1)

# Print the roots of the second function
print("Roots of cos(2x) * x^3 = 0:", roots_func2)

# Print the intersection points if any
if intersection_points:
    print("The functions intersect at the following point(s):", intersection_points)
else:
    print("The functions do not intersect within the specified range.")
