"""
Solve Project Euler Problem 80

Find digital sum of irrational square roots.

"""

import itertools
import math
import textwrap

def pair_stream(n):
    """Return an infinite stream of digits paired from n"""
    n_str = str(n)
    if len(n_str) % 2 != 0:
        n_str = '0' + n_str
    pairs = textwrap.wrap(n_str, 2)
    digit_pairs = [int(p) for p in pairs]
    return itertools.chain(digit_pairs, itertools.repeat(0))

def root_stream(n):
    pairs = pair_stream(n)

    remainder = 0
    p         = 0
    while True:
        c = remainder * 100 + pairs.next()
        x = find_x(p, c)
        y = (20*p + x)*x
        p = (p*10) + x
        yield x
        remainder = c - y
        if remainder == 0:
            raise StopIteration

def find_x(p, c):
    """Find the largest integer x so that (20*p + x)*x does not exceed c."""
    if p == 0:
        x = int(math.sqrt(c)) + 1
    else:
        x = int(c / (20. * p)) + 1
    while True:
        y = (20 * p + x)*x
        if y <= c:
            return x
        else:
            x -= 1

def digital_sum(n, num_digits):
    r = root_stream(n)
    s = 0
    for i in range(num_digits):
        v = r.next()
        s += v
    return s

def solve():
    total = 0
    for num in range(2, 100):
        try:
            total += digital_sum(num, 100)
        except StopIteration:
            total += 0    
    return total

def main():
    print solve()

if __name__ == "__main__":
    main()
