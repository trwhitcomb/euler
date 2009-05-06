"""
Solve Project Euler Problem 227

Find the expected number of terms that "The Chase" game lasts

"""

from __future__ import division

import numpy as np

def generate_matrices(num_players):
    main_diag = 1       * np.ones(num_players  )
    diag_1    = (-4/9)  * np.ones(num_players-1)
    diag_2    = (-1/18) * np.ones(num_players-2)
    diag_m1   = (-4/9)  * np.ones(1)
    diag_m2   = (-1/18) * np.ones(2)

    A = (np.diag(main_diag, k=0 ) + 
         np.diag(diag_1,    k=1 ) +
         np.diag(diag_1,    k=-1) +
         np.diag(diag_2,    k=2 ) +
         np.diag(diag_2,    k=-2) +
         np.diag(diag_m2,   k=num_players-2) +
         np.diag(diag_m1,   k=num_players-1) +
         np.diag(diag_m2,   k=-num_players+2) +
         np.diag(diag_m1,   k=-num_players+1))
    A[0,:] = 0
    A[0,0] = 1

    """
    A = np.zeros((num_players, num_players))
    A[0,0] = 1
    for i in np.arange(1,num_players):
        A[i, i            ] = 1
        A[i, np.mod(i+1,num_players)] = -4/9
        A[i, np.mod(i-1,num_players)] = -4/9
        A[i, np.mod(i+2,num_players)] = -1/18
        A[i, np.mod(i-2,num_players)] = -1/18
    """
    b = np.ones(num_players)
    b[1:] *= 2
    return A, b

def solve(num_players):
    A, b  = generate_matrices(num_players)

    x = np.linalg.solve(A,b)
    return x
