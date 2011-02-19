"""
Solve Project Euler Problem 317

Find the volume of of the region travelled by a firecracker fragments

"""

import sys

import matplotlib.pylab as plt
import numpy as np

X_0 = 0.0       # meters
Y_0 = 100.0     # meters
V_0 = 20.0      # meters/second

G = -9.81       # meters/second^2

TIME_SAMPLE_COUNT  = 500
ANGLE_SAMPLE_COUNT = 100
MIN_ANGLE          = 0.0
MAX_ANGLE          = np.pi/2

def solve_quad(a, b, c):
    """Solve quadratic equation ax^2 + bx + c = 0"""
    discriminant = b**2 - 4*a*c
    return ((-b+np.sqrt(discriminant))/(2.0*a), 
            (-b-np.sqrt(discriminant))/(2.0*a))

def trace_path(angle, times=None):
    """
    Given the angle of departure, compute the path through 2-D space
    of a firework fragment.

    """
    if times is None:
        t_max = airtime(angle)
        print "t_max is", t_max
        times = np.linspace(0, t_max, TIME_SAMPLE_COUNT)

    # Find the longest time aloft
    v0_x = V_0 * np.cos(angle)
    v0_y = V_0 * np.sin(angle)

    x = v0_x*times + X_0
    y = G*times**2 + v0_y*times + Y_0
    #y[y < 0] = 0.0
    return x, y

def airtime(angle):
    """Given the angle of departure, compute the time the particle is aloft."""
    v0_x = V_0 * np.sin(angle)
    v0_y = V_0 * np.cos(angle)
    times = solve_quad(G, v0_y, Y_0)
    print times
    t_max = np.max(times)
    return t_max

def solve():
    angles = np.linspace(MIN_ANGLE, MAX_ANGLE, ANGLE_SAMPLE_COUNT)
    times  = np.array([airtime(angle) for angle in angles])

    t      = np.linspace(0, max(times), TIME_SAMPLE_COUNT)
    x      = np.zeros((ANGLE_SAMPLE_COUNT, TIME_SAMPLE_COUNT))
    y      = np.zeros((ANGLE_SAMPLE_COUNT, TIME_SAMPLE_COUNT))

    for (i, angle) in enumerate(angles):
        x[i,:], y[i,:] = trace_path(angle, t)
        plt.plot(x[i,y[i,:]>=0], y[i,y[i,:]>=0])
    plt.show()

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    solve()
    return

    x, y = trace_path(np.pi/4)
    import matplotlib.pylab as plt
    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    main()
