#!/usr/bin/env python

"""
<p>The prime factors of $13195$ are $5, 7, 13$ and $29$.</p>
<p>What is the largest prime factor of the number $600851475143$?</p>

"""

import sieve

target = 600851475143
#target = 13195

primes = sieve.primes_below(int(target**0.5))
factors = []
while target > 1:
    prime = next(primes)
    if target % prime == 0:
        # found a factor!
        factors.append(prime)
        target /= prime
print(factors)