#!/usr/bin/env python

"""
<p>$2520$ is the smallest number that can be divided by each of the numbers from $1$ to $10$ without any remainder.</p>
<p>What is the smallest positive number that is <strong class="tooltip">evenly divisible<span class="tooltiptext">divisible with no remainder</span></strong> by all of the numbers from $1$ to $20$?</p>
"""

def check_divisible(check_number, divisors):
    """
    Return True if check_number is evenly divisible by all of the divisors.

    """
    evenly_divisible = False
    for divisor in divisors:
        if check_number % divisor:
            # nonzero remainder - so it's not an even division
            break
    else:
        evenly_divisible = True
    return evenly_divisible

n = 10
test_divisors = [i+1 for i in range(20)]
while True:
    if check_divisible(n, test_divisors):
        print(n)
        break
    else:
        n += 1
