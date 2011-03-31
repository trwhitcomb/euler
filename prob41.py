"""
Solve Project Euler Problem 41

Find pandigital primes

"""

import itertools
import math
import pprint

def is_prime(n):
    if n % 2 == 0:
        return False
    divisors = xrange(3, int(math.sqrt(n)), 2)
    for d in divisors:
        if n % d == 0:
            return False
    return True 

def generate_pandigitals(num_digits):
    digits      = ['%d' % (d+1) for d in range(num_digits)]
    combos      = itertools.permutations(digits)
    for c in combos:
        yield int(''.join(c))

def solve():
    digits = xrange(4, 10)
    pandigital_primes = {}
    for d in digits:
        pandigitals = generate_pandigitals(d)
        pandigital_primes[d] = [p for p in pandigitals if is_prime(p)]
        print pandigital_primes[d]
            
    pprint.pprint(pandigital_primes)

if __name__ == "__main__":
    solve()
