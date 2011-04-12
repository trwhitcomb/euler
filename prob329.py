"""
Solve Project Euler Problem 329

Find the probability of a sequence coming from the prime frog.

"""

import fractions
import itertools
import sys

import numpy as np

## {{{ http://code.activestate.com/recipes/117119/ (r2)
# Sieve of Eratosthenes
# David Eppstein, UC Irvine, 28 Feb 2002

def eratosthenes():
	'''Yields the sequence of prime numbers via the Sieve of Eratosthenes.'''
	D = {}  # map composite integers to primes witnessing their compositeness
	q = 2   # first integer to test for primality
	while 1:
		if q not in D:
			yield q        # not marked composite, must be prime
			D[q*q] = [q]   # first multiple of q not already marked
		else:
			for p in D[q]: # move each witness to its next multiple
				D.setdefault(p+q,[]).append(p)
			del D[q]       # no longer need D[q], free memory
		q += 1
## end of http://code.activestate.com/recipes/117119/ }}}

def primes_below(n):
    sieve  = eratosthenes()
    return list(itertools.takewhile(lambda p: p<n, sieve))
    
def compute_probabilities(n, state):
    """
    Compute the probability of seeing a P or N come from the frog for a 
    given state.

    """
    primes_below_n = primes_below(n)
    #print primes_below_n
    num_primes = len(primes_below(n))
    #print num_primes, n
    
    prime_indices    = [i for i in range(n) if i+1 in primes_below_n]
    notprime_indices = [i for i in range(n) if i+1 not in primes_below_n]

    #print prime_indices
    #print notprime_indices
    # Conditional probabilities for getting a P or an N if the frog is
    # on a prime or non-prime square
    prob_P_prime    = fractions.Fraction(2, 3)
    prob_N_prime    = fractions.Fraction(1, 3)
    prob_P_notprime = fractions.Fraction(1, 3)
    prob_N_notprime = fractions.Fraction(2, 3)

    prob_prime    = np.sum(state[prime_indices])
    prob_notprime = np.sum(state[notprime_indices])

    prob_P = prob_P_prime*prob_prime + prob_P_notprime*prob_notprime
    prob_N = prob_N_prime*prob_prime + prob_N_notprime*prob_notprime
    assert(prob_P + prob_N == 1)

    return prob_P, prob_N

def make_transition_matrix(n):
    diag = [fractions.Fraction(1, 2) for i in range(n-1)]

    upper_diag     = diag[:]
    upper_diag[-1] = fractions.Fraction(1, 1)
    lower_diag     = diag[:]
    lower_diag[0]  = fractions.Fraction(1, 1)

    return np.diag(upper_diag, k=1) + np.diag(lower_diag, k=-1)

def make_initial_condition(n):
    x = [fractions.Fraction(1, n) for i in range(n)]
    return np.array(x)

def solve():
    board_size = 500

    A = make_transition_matrix(board_size)
    x = make_initial_condition(board_size)
    #outcome = 'PPPPNNPPPNPPNPN' 
    outcome = 'PPPPNNPP'
    prob = {}
    p = fractions.Fraction(1, 1)
    for croak in outcome:
        prob['P'], prob['N'] = compute_probabilities(board_size, x)
        p *= prob[croak]
        x = np.dot(A, x)
    print p
        

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    solve()

if __name__ == "__main__":
    main()
