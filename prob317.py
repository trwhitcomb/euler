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

TIME_SAMPLE_COUNT  = 20000
ANGLE_SAMPLE_COUNT = 2000
MIN_ANGLE          = 0.0
MAX_ANGLE          = np.pi/2

X_POINTS = 20000

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
    return x, y

def airtime(angle):
    """Given the angle of departure, compute the time the particle is aloft."""
    v0_x = V_0 * np.sin(angle)
    v0_y = V_0 * np.cos(angle)
    times = solve_quad(G, v0_y, Y_0)
    t_max = np.max(times)
    return t_max

def generate_path_set():
    angles = np.linspace(MIN_ANGLE, MAX_ANGLE, ANGLE_SAMPLE_COUNT)
    times  = np.array([airtime(angle) for angle in angles])

    t      = np.linspace(0, max(times), TIME_SAMPLE_COUNT)
    x      = np.zeros((ANGLE_SAMPLE_COUNT, TIME_SAMPLE_COUNT))
    y      = np.zeros((ANGLE_SAMPLE_COUNT, TIME_SAMPLE_COUNT))

    for (i, angle) in enumerate(angles):
        x[i,:], y[i,:] = trace_path(angle, t)

    return x, y

def interpolate_curves(x_raw, y_raw):
    x_interp = np.linspace(0, np.max(x_raw), X_POINTS)

    y_interp = []
    for x, y in zip(x_raw, y_raw):
        y_interp.append(np.interp(x_interp, x, y))
    return x_interp, np.array(y_interp)

def generate_bounding_curve(x_interp, y_interp):
    y_bound = y_interp.max(axis=0)

    criteria = y_bound >= 1E-10
    y_bound = y_bound[criteria]
    x_bound = x_interp[criteria]
    return x_bound, y_bound

def do_solid_integration(x_bound, y_bound):
    f = x_bound * y_bound
    return 2*np.pi * np.trapz(f, x_bound)
    
def solve():
    x_raw, y_raw = generate_path_set()

    x_interp, y_interp = interpolate_curves(x_raw, y_raw)
    x_bound, y_bound = generate_bounding_curve(x_interp, y_interp)
    plt.plot(x_bound, y_bound, 'k-')
    print do_solid_integration(x_bound, y_bound)
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
