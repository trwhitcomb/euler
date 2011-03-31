"""
Solve Project Euler Problem 104

Pandigital numbers in Fibonacci numbers

"""

is_pandigital = lambda s: ''.join(sorted(s)) == '123456789'

def fib_stream():
    a, b = 1L, 1L
    while True:
        yield a
        a, b = b, a+b

def solve():
    fibs = fib_stream()
    for i, f in enumerate(fibs):
        if i % 1000 == 0:
            print i
        s = str(f)
        first_9 = s[:9]
        last_9  = s[-9:]
        if is_pandigital(first_9) and is_pandigital(last_9):
            print 'Answer is %d' % i+1
            return
