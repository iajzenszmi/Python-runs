import numpy as np
from scipy.optimize import brentq

def zbrent(func, x1, x2, TOL=1e-5):
    """Finds the root of a function known to lie between x1 and x2 using Brent's method.

    Args:
    func (function): The function for which the root is to be calculated.
    x1 (float): The lower limit of the bracket.
    x2 (float): The upper limit of the bracket.
    TOL (float, optional): The desired accuracy. Defaults to 1e-5.

    Returns:
    float: The root of the function.
    """
    root, results = brentq(func, x1, x2, full_output=True, xtol=TOL)

    if results.converged:
        return root
    else:
        raise ValueError(f"The root finding process did not converge after {results.iterations} iterations.")

# Test with a function
def test_func(x):
    return x**2 - 4

root = zbrent(test_func, 0, 3)
print("Root of the function: ", root)

