"""
Solve Project Euler Problem 228

Find Minkowski sum of large polygons

Tolerance necessary for solution: 1E-12

"""

from __future__ import division

import numpy as np

def deg2rad(x):
    return x * (np.pi / 180.0)

def gen_vertices(n):
    """Return set of direction vectors that form polygon S_n."""

    k      = np.arange(n) + 1
    theta  = deg2rad((2*k - 1) * (180.0/n))
    x      = np.cos(theta)
    y      = np.sin(theta)
    dx     = np.roll(x, -1) - x
    dy     = np.roll(y, -1) - y
    dtheta = np.roll(theta, -1) - theta
    #return zip(theta, dtheta)
    return zip(theta, dx, dy)

def join(graph_1, graph_2):
    """Minkowki sum two polygons."""

    j = graph_1 + graph_2
    # Sort by polar angle
    j.sort(key=lambda x:x[0])
    return j

def is_parallel(v1,v2,tol):
    cos_theta = (np.linalg.norm(v1) * np.linalg.norm(v2)) / np.dot(v1,v2) 
    # If the angle is zero, cos(theta) is 1
    return abs(cos_theta - 1.0) < tol

def count_edges(graph, parallel_tol):
    """Count edges of a graph."""

    count     = len(graph)
    cur_edge  = np.array(graph)
    next_edge = np.roll(np.array(graph), -1, axis=0)
    for i in xrange(len(graph)):
        # See if the vertices are parallel
        e1 = cur_edge[i,1:]
        e2 = next_edge[i,1:]
        if is_parallel(e1, e2, parallel_tol):
            count -= 1
        #print('%s:%s - %s' % (e1, e2, is_parallel(e1, e2)))
    return count

def main(tol=1.0e-5):
    S_sum = []
    print('Generating graphs...')
    for n in xrange(1864, 1910):
        S_sum = join(S_sum, gen_vertices(n))
    print('Counting edges...')
    edges = count_edges(S_sum, tol)
    print('Edges: %d' % edges)
    return (S_sum, edges)

if __name__ == "__main__":
    main()
