#!/usr/bin/env python

import collections
import itertools

## {{{ http://code.activestate.com/recipes/117119/ (r2)
# Sieve of Eratosthenes
# David Eppstein, UC Irvine, 28 Feb 2002

def eratosthenes():
    """
    Iterator form of the Sieve of Eratosthenes.
    
    Yields the sequence of prime numbers. Originally from:
        http://code.activestate.com/recipes/117119/ (r2)
        David Eppstein, UC Irvine, 28 Feb 2002

    """
    D = collections.defaultdict(list)
    q = 2   # first integer to test for primality
    while True:
        if q not in D:
            yield q        # not marked composite, must be prime
            D[q*q] = [q]   # first multiple of q not already marked
        else:
            for p in D[q]: # move each witness to its next multiple
                D[p+q].append(p)
            del D[q]       # no longer need D[q], free memory
        q += 1 

def primes_below(n):
    """
    Generate a list of prime numbers below a certain value.
    """
    my_sieve = eratosthenes()
    return itertools.takewhile(lambda p: p<n, my_sieve)