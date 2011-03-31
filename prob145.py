"""
Solve Project Euler Problem 145

Find reversible numbers

"""

class ReverseError(Exception):  pass

def compute_reverse(n):
    n_str = str(n)
    n_str_rev = ''.join(reversed(n_str))
    if n_str_rev[0] == '0':
        raise ReverseError('Cannot have a leading zero!')
    return int(n_str_rev)

def check_odd_digits(n):
    return all([int(d) % 2 != 0 for d in str(n)])

def check_reversible(n):
    try:
        n_rev = compute_reverse(n)
    except ReverseError:
        return False
    return check_odd_digits(n + n_rev)

def main():
    count = 0
    for i in xrange(1000000000):
        if check_reversible(i):
            count += 1
    print count
    
if __name__ == "__main__":
    main()
