#!/usr/bin/env python

import sieve

primes = sieve.eratosthenes()

prime_sum = 0
for prime in primes:
    if prime > 2000000:
        break
    prime_sum += prime
print(prime_sum)