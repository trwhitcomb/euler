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

TIME_SAMPLE_COUNT  = 100
ANGLE_SAMPLE_COUNT = 25
MIN_ANGLE          = 0.0
MAX_ANGLE          = np.pi/2

######################################################################

import numpy as n, pylab as p, time

def _angle_to_point(point, centre):
    '''calculate angle in 2-D between points and x axis'''
    delta = point - centre
    res = n.arctan(delta[1] / delta[0])
    if delta[0] < 0:
        res += n.pi
    return res


def _draw_triangle(p1, p2, p3, **kwargs):
    tmp = n.vstack((p1,p2,p3))
    x,y = [x[0] for x in zip(tmp.transpose())]
    p.fill(x,y, **kwargs)
    #time.sleep(0.2)


def area_of_triangle(p1, p2, p3):
    '''calculate area of any triangle given co-ordinates of the corners'''
    return n.linalg.norm(n.cross((p2 - p1), (p3 - p1)))/2.


def convex_hull(points, graphic=True, smidgen=0.0075):
    '''Calculate subset of points that make a convex hull around points

Recursively eliminates points that lie inside two neighbouring points until only convex hull is remaining.

:Parameters:
    points : ndarray (2 x m)
        array of points for which to find hull
    graphic : bool
        use pylab to show progress?
    smidgen : float
        offset for graphic number labels - useful values depend on your data range

:Returns:
    hull_points : ndarray (2 x n)
        convex hull surrounding points
'''
    if graphic:
        p.clf()
        p.plot(points[0], points[1], 'ro')
    n_pts = points.shape[1]
    assert(n_pts > 5)
    centre = points.mean(1)
    if graphic: p.plot((centre[0],),(centre[1],),'bo')
    angles = n.apply_along_axis(_angle_to_point, 0, points, centre)
    pts_ord = points[:,angles.argsort()]
    if graphic:
        for i in xrange(n_pts):
            p.text(pts_ord[0,i] + smidgen, pts_ord[1,i] + smidgen, \
                   '%d' % i)
    pts = [x[0] for x in zip(pts_ord.transpose())]
    prev_pts = len(pts) + 1
    k = 0
    while prev_pts > n_pts:
        prev_pts = n_pts
        n_pts = len(pts)
        if graphic: p.gca().patches = []
        i = -2
        while i < (n_pts - 2):
            Aij = area_of_triangle(centre, pts[i],     pts[(i + 1) % n_pts])
            Ajk = area_of_triangle(centre, pts[(i + 1) % n_pts], \
                                   pts[(i + 2) % n_pts])
            Aik = area_of_triangle(centre, pts[i],     pts[(i + 2) % n_pts])
            if graphic:
                _draw_triangle(centre, pts[i], pts[(i + 1) % n_pts], \
                               facecolor='blue', alpha = 0.2)
                _draw_triangle(centre, pts[(i + 1) % n_pts], \
                               pts[(i + 2) % n_pts], \
                               facecolor='green', alpha = 0.2)
                _draw_triangle(centre, pts[i], pts[(i + 2) % n_pts], \
                               facecolor='red', alpha = 0.2)
            if Aij + Ajk < Aik:
                if graphic: p.plot((pts[i + 1][0],),(pts[i + 1][1],),'go')
                del pts[i+1]
            i += 1
            n_pts = len(pts)
        k += 1
    return n.asarray(pts)

######################################################################
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

def solve():
    angles = np.linspace(MIN_ANGLE, MAX_ANGLE, ANGLE_SAMPLE_COUNT)
    times  = np.array([airtime(angle) for angle in angles])

    t      = np.linspace(0, max(times), TIME_SAMPLE_COUNT)
    x      = np.zeros((ANGLE_SAMPLE_COUNT, TIME_SAMPLE_COUNT))
    y      = np.zeros((ANGLE_SAMPLE_COUNT, TIME_SAMPLE_COUNT))

    for (i, angle) in enumerate(angles):
        x[i,:], y[i,:] = trace_path(angle, t)
        #plt.plot(x[i,y[i,:]>=0], y[i,y[i,:]>=0], '.')


    num_points = len(y[y>=0].flat)

    points = np.zeros((2, num_points + 1))
    points[0, 0] = 0.0
    points[1, 0] = 0.0
    points[0, 1:] = (x[y>=0]).flat
    points[1, 1:] = (y[y>=0]).flat
    plt.ion()
    hull_pts = convex_hull(points, True)
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
