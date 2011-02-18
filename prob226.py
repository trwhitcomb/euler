"""
Solve Project Euler Problem 226

Find areal intersection of a circle and the Blancmage curge

"""

import numpy as np
import scipy.interpolate

# Experiment parameters
CIRCLE_RADIUS   = 0.25
CIRCLE_CENTER_X = 0.25
CIRCLE_CENTER_Y = 0.5

def blanc(d):
    """
    Define the d-th iteration of the Blancmage function
    (see http://mathworld.wolfram.com/BlancmangeFunction.html)
    """
    N = 2**d
    b = np.zeros(N+1)
    for n in xrange(d, 0, -1):
        for k in xrange(0, N/2**n):
            m = k * 2**n
            b[m+2**(n-1)] = 2**n + 0.5 * (b[m] + b[m+2**n])

    # b is calculated, now normalize to the unit interval
    return np.linspace(0.0, 1.0, num=N+1), b * 2**(-(d+1))

def between_curves():
    # Return the distance between the circle and the Blancmange curve
    # at each point within the first half of the interval

    x_trim   = x_blanc[x_blanc <= 0.5]
    y_trim   = y_blanc[x_blanc <= 0.5]

    # Equation for the circle is
    # (x-x_center)**2 + (y-y_center)**2 = radius**2
    y_circle = (-np.sqrt(CIRCLE_RADIUS**2 - (x_trim - CIRCLE_CENTER_X)**2) + 
                CIRCLE_CENTER_Y)

    new_x = x_trim[y_trim >= y_circle]
    new_y = y_trim[y_trim >= y_circle]
    distance = (y_trim - y_circle)[y_trim >= y_circle]

    area = np.trapz(distance, new_x)
    print area

if __name__ == "__main__":
    for i in range(22, 30):
        x_blanc, y_blanc = blanc(i)
        between_curves()

