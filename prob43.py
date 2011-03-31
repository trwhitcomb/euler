"""
Solve Project Euler Problem 43

Find pandigitals with certain divisor properties

"""

import itertools
import math
import pprint

def generate_pandigital_segments(num_digits):
    digits      = ['%d' % (d) for d in range(num_digits)]
    combos      = itertools.permutations(digits)
    for c in combos:
        segments = make_segments(c)
        yield int(''.join(c)), segments

def make_segments(num_str):
    bounds = [(i+1, i+4) for i in range(7)]
    segments = [int(''.join(num_str[start:end])) for (start, end) in bounds]
    return segments
    
def check_divisible(segments):
    divisors = [2, 3, 5, 7, 11, 13, 17]
    for seg, div in zip(segments, divisors):
        if seg % div != 0:
            return False
    return True

def solve():
    has_prop = []
    for p, s in generate_pandigital_segments(10):
        if check_divisible(s):
            print p
            has_prop.append(p)
    
    print has_prop
    print sum(has_prop)

if __name__ == "__main__":
    solve()
