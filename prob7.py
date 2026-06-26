#!/usr/bin/env python

import sieve

prime_iter = sieve.eratosthenes()

for _ in range(10000):
    next(prime_iter)
print(next(prime_iter))
