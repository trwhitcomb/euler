"""
Solve Project Euler Problem 235

Let s(n) be \sum_{k=1}^{n} u(k) where
u(k) = (900 - 3k) * r^{k-1}

Find value of r to make s(5000) = -6E11

"""

from __future__ import division

import scipy.optimize as opt
import numpy as np

def test_func(n, r):
    s_iter = 0
    u = lambda k: (900 - 3*k)*r**(k-1)
    for k in (np.arange(n) + 1):
        s_iter += u(k)
    s_calc = func(r, n, 0)
    print('%s %s' % (s_iter, s_calc))

def dfunc(r, n, target):
    """Compute d/dr s(n) - provide Jacobian for fsolve."""
    print((r, n, target))
    low   = (1-r)**2
    dlow  = -2 * (1-r)
    high  = 897 - 900*r + 900*r**2 + r**n*(3*n - 897 - 3*n*r)
    dhigh = -900 + 2*900*r + n*(3*n-897)*r**(n-1) - 3*n*(n+1)*r**n
    return (low*dhigh - high*dlow) / (low**2)

def func(r, n, target):
    """Compute s(n) - target using r."""

    # Compute first term:
    # 900 \sum_{k=1}^{n} r^{k-1}
    term1 = 900 * ((1 - r**n) / (1 - r))

    # Compute second term:
    # 3 \sum_{k=1}^{n} k r^{k-1}
    # which can be computed using
    # d/dr \sum_{k=0}^{n} r^{k}
    sum_numer = 1 - r**(n+1) - (n+1)*r**n + (n+1)*r**(n+1)
    sum_denom = (1 - r) ** 2
    term2     = 3 * (sum_numer / sum_denom)

    return (term1 - term2) - target

def solve(n, sum):
    """Solve for r to make s(n) == sum."""

    # r ranges from 0 to 1
    x = opt.fsolve(func, x0=(1.001), args=(n,sum),xtol=1.0e-14,
                   fprime=dfunc, col_deriv=1, maxfev=1000)
    return (x)
