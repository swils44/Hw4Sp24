import numpy as np
from scipy.optimize import fsolve

#I collaborated with ChatGPT to create this code. This is the code that Chat gave me. I told it that it could use
#numpy and scipy to write the code.

def func1(x):
    """
    Here, we are defining our first function: x - 3cos(x)

    Parameters:
    x (float or array_like): Input value(s) for which the function value is calculated.

    Returns:
    float or array_like: Value(s) of the function at the input value(s) x.
    """
    return x - 3 * np.cos(x)  # Using np.cos to handle array-like input

def func2(x):
    """
    Here, we are defining our first function: cos(2x) * x^3

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

# Print the roots of the first function
print("Roots of x - 3cos(x) = 0:", roots_func1)

# Print the roots of the second function
print("Roots of cos(2x) * x^3 = 0:", roots_func2)
