#!/usr/bin/env python

# Longest Collatz
# This sequence will be predictable when it hits a given number
# (i.e. starting with 13 will always produce the same sequence).
# So, we can memoize the length and only have to compute the
# sequence once

import functools

@functools.cache
def collatz_length(n):
    if n == 1:
        return 1
    if n % 2:
        next_n = 3*n + 1
    else:
        next_n = n / 2
    return 1 + collatz_length(next_n)

print(collatz_length(13))

max_length = 0
for i in range(1000000):
    length = collatz_length(i+1)
    if length > max_length:
        starter = i+1
        max_length = length
print(starter, max_length)

