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

## {{{ Generate prime numbers below a certain value
def primes_below(n):
    sieve  = eratosthenes()
    return list(itertools.takewhile(lambda p: p<n, sieve))
## }}}
    
def compute_probabilities(n, state):
    """
    Compute the probability of seeing a P or N come from the frog for a 
    given state.

    """
    primes_below_n = primes_below(n)
    
    prime_indices    = np.array([i+1 in primes_below_n for i in range(n)])
    notprime_indices = np.array([i+1 not in primes_below_n for i in range(n)])

    # Conditional probabilities for getting a P or an N if the frog is
    # on a prime or non-prime square
    prob_P_prime    = fractions.Fraction(2, 3)
    prob_N_prime    = fractions.Fraction(1, 3)
    prob_P_notprime = fractions.Fraction(1, 3)
    prob_N_notprime = fractions.Fraction(2, 3)

    assert(np.sum(state) == 1)
    prob_prime    = np.sum(state[prime_indices])
    prob_notprime = np.sum(state[notprime_indices])
    assert(prob_prime + prob_notprime == 1)

    prob_P = prob_P_prime*prob_prime + prob_P_notprime*prob_notprime
    prob_N = prob_N_prime*prob_prime + prob_N_notprime*prob_notprime
    assert(prob_P + prob_N == 1)

    return prob_P, prob_N

def make_transition_matrix(n):

    # Off-diagonal means it's 1 shorter than the main diagonal
    diag = [fractions.Fraction(1, 2) for i in range(n-1)]

    # Upper diagonal is .5 .5 .5 .5 ... 1.
    # Lower diagonal is 1. .5 .5 .5 ... .5
    upper_diag     = diag[:]
    upper_diag[-1] = fractions.Fraction(1, 1)
    lower_diag     = diag[:]
    lower_diag[0]  = fractions.Fraction(1, 1)

    return np.diag(upper_diag, k=1) + np.diag(lower_diag, k=-1)

def make_initial_condition(n, nonzero=None):
    if nonzero is None:
        x = [fractions.Fraction(1, n) for i in range(n)]
    else:
        x = [fractions.Fraction(0, 1) for i in range(n)]
        x[nonzero] = fractions.Fraction(1, 1)
    return np.array(x)

def solve(outcome='PPPPNNPPPNPPNPN'):
    board_size = 500

    A = make_transition_matrix(board_size)
    x = make_initial_condition(board_size)
    #outcome = 
    #outcome = 'PP'
    prob = {}
    p = fractions.Fraction(1, 1)
    croak_result = ''
    for croak in outcome:
        prob['P'], prob['N'] = compute_probabilities(board_size, x)
        print 'P(%s) = %s' % (croak, prob[croak])
        p *= prob[croak]
        croak_result += croak
        print 'P(%s) = %s' % (croak_result, p)
        x = np.dot(A, x)
    print float(p)

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    solve()


#### Monte Carlo Simulation

import random

class Frog:

    # The frog croaks the correct prime/nonprime with probability 2/3
    CROAK_ON_PRIME    = ('P', 'P', 'N')
    CROAK_ON_NONPRIME = ('N', 'N', 'P')

    def __init__(self, board_size=500):
        self.primes   = primes_below(board_size)
        self.position = random.randrange(board_size)    

        # Each square has a possible move to the adjacent squares, but
        # the endpoints only have a single possible move.
        self.possible_moves     = [(-1, +1) for _ in range(board_size)]
        self.possible_moves[0]  = (+1,)
        self.possible_moves[-1] = (-1,)

    def jump(self):
        move = random.choice(self.possible_moves[self.position])
        self.position += move

    def croak(self):
        square_num = self.position + 1
        if square_num in self.primes:
            return random.choice(Frog.CROAK_ON_PRIME)
        else:
            return random.choice(Frog.CROAK_ON_NONPRIME)

    def __iter__(self):
        while True:
            yield self.croak()
            self.jump()

# Serial Version
def run(ref_string, num_trials=50000):
    results = [trial(ref_string) for _ in xrange(num_trials)]
    num_correct = results.count(True)
    prob_correct = float(num_correct) / float(num_trials)
    print ('%d correct out of %d trials: p(%s) = %f' % 
           (num_correct, num_trials, ref_string, prob_correct))
    return prob_correct 

def trial(croak_string):
    frog = Frog()
    for (ref_croak , croak) in zip(croak_string, frog):
        if ref_croak != croak:
            return False
    return True

# Parallel Version
import multiprocessing
import Queue

def run_parallel(ref_string, num_trials=50000):
    result_queue = multiprocessing.Queue()

    pool = multiprocessing.Pool(initializer=parallel_init, 
                                initargs=(result_queue,))
    ref_strings = (ref_string for _ in xrange(num_trials)) 
    pool.imap(parallel_trial, ref_strings, chunksize=100)
    pool.close()
    results = process_queue(result_queue)
    pool.join()

    num_correct = results.count(True)
    prob_correct = float(num_correct) / float(num_trials)
    print ('%d correct out of %d trials: p(%s) = %f' % 
           (num_correct, num_trials, ref_string, prob_correct))
    return prob_correct 

def process_queue(q):
    results = []
    try:
        while True:
            results.append(q.get(block=True, timeout=0.5))
    except Queue.Empty:
        pass
    return results

def parallel_trial(croak_string):
    result = trial(croak_string)
    parallel_trial.q.put(result)
    
def parallel_init(q):
    parallel_trial.q = q

if __name__ == "__main__":
    #outcome = 'PPPPNNPPPNPPNPN' 
    outcome = 'PP' 
    #probs = [run(outcome, num_trials=50000) for _ in range(10)]
    probs = [run_parallel(outcome, num_trials=500000) for _ in range(500)]
    total_prob = sum(probs) / len(probs)
    print total_prob
    
    solve(outcome='PP') 
    #main()

