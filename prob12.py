#!/usr/bin/env python

import numpy as np

n = 4626

while True:
    triangle = np.sum(np.arange(1,n+1))
    triangle_divisors = np.arange(1,triangle+1)
    remainders = np.mod(triangle, triangle_divisors)
    num_divisors = np.count_nonzero(remainders == 0)
    if n % 5000 == 0:
        print(n, triangle, num_divisors)
    if num_divisors > 500:
        break
    n += 1
print(n, triangle, num_divisors)