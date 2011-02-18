"""
Solve Project Euler Problem 226

Find areal intersection of a circle and the Blancmage curge

"""

from __future__ import division

import numpy as np
from scipy.signal import cspline1d, cspline1d_eval
import scipy.interpolate

# Experiment parameters
CIRCLE_RADIUS   = 0.25
CIRCLE_CENTER_X = 0.25
CIRCLE_CENTER_Y = 0.5
CIRCLE_AREA     = np.pi * CIRCLE_RADIUS * CIRCLE_RADIUS

def pol2rec(r, theta):
    """
    Convert polar coordinates to their rectangular form
    """
    return r*np.cos(theta), r*np.sin(theta) 

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

def gen_points(n):
    """
    Generate n random points within the circle
    """
    rad   = np.random.rand(n)
    angle = np.random.rand(n)
    
    # Normalize for the appropriate ranges - make sure that the 
    # distribution is proper
    # (see http://mathworld.wolfram.com/DiskPointPicking.html
    rad   = np.sqrt(rad*(CIRCLE_RADIUS**2))
    angle = angle * 2*np.pi
    
    # Convert to rectangular coordinates
    x, y = pol2rec(rad, angle)

    # Recenter the circle
    x += CIRCLE_CENTER_X
    y += CIRCLE_CENTER_Y

    return x, y

def mc_int(n):
    """
    Integrate the intersection using Monte Carlo methods with n sample points
    """
    
    # Generate random points within the circle
    x_m, y_m = gen_points(n)

    # Get the value of the blancmage curve at these points
    y_b = compute_y(x_m)

    return np.ma.MaskedArray(np.ones(n), mask=y_b>y_m).count()

def diagnose(n):
    """
    Show this taking place
    """
    from matplotlib.patches import Circle
    import pylab
    pylab.plot(x_blanc, y_blanc)
    a = pylab.gca()
    a.add_patch(Circle((CIRCLE_CENTER_X, CIRCLE_CENTER_Y),
                radius=CIRCLE_RADIUS, fill=False))
    x_d, y_d = gen_points(n)
    pylab.plot(x_d, y_d, '.')
    y_b = compute_y(x_d)
    pylab.plot(x_d, y_b, '.') 
    pylab.show()
    return y_d, y_b

def update(total, under_curve, prev_area):
    """
    Updates the area guess and the error
    """
    area = CIRCLE_AREA * under_curve / total
    abs_error = np.abs(prev_area - area)
    print('%d %d %11.10f %11.10f' % (total, under_curve, area, abs_error))
    return area, abs_error

def solve(points_per_trial, continuous=False, total_points=0, 
          points_within_curve=0):
    """
    Solve the problem, using the given number of trials for the Monte
    Carlo integration
    """

    err                 = 1
    area = 1.0

    if continuous:
        def cont_exp(err):
            return True
    else:
        def cont_exp(err):
            return err > 1.0E-10

    while cont_exp(err):
        total_points        += points_per_trial
        points_within_curve += mc_int(points_per_trial)
        area,err = update(total_points, points_within_curve, area)
         
    print(area)
    return area

x_blanc, y_blanc = blanc(21)
compute_y        = scipy.interpolate.interp1d(x_blanc, y_blanc)
