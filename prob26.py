
"""
Solve Problem 26.

"""

# Long division algorithm

import itertools

def generate_digits(original_value):
    """
    Given an integer value, returns the values of each digit in sequence,
    followed by a sequence of zeroes.  A None value in the stream signifies
    the end of the original digits
    """
    value_digits = (int(d) for d in str(original_value))
    all_zeroes   = itertools.repeat(0)
    return itertools.chain(value_digits, all_zeroes)

def remainder_stream(a, b):
    r = 0
    for next_digit in generate_digits(a):
        r = r*10 + next_digit
        if r == 0:
            raise StopIteration
        q, r = divmod(r, b)
        yield r

def repeat_length(a, b):
    """
    Return the length of the repeating portion of the decimal representation
    of a / b.  Returns zero if the decimal terminates.

    """
    digits     = list()
    remainders = remainder_stream(a, b)
    #print '*', a, b
    all_zero = True
    try:
        while True:
            next_digit = remainders.next()
            if all_zero and next_digit != 0:
                all_zero = False
            if not all_zero:
                #print next_digit, digits
                if next_digit in digits:
                    digit_pos = digits.index(next_digit)
                    return len(digits[digit_pos:])
                else:
                    digits.append(next_digit)
    except StopIteration:
        return 0

def max_repeat_len(d):
    trials = range(1, d+1)
    l      = [repeat_length(1, n) for n in trials]
    max_value = max(l)
    print trials[l.index(max_value)]
    #print zip(trials, l)

if __name__ == "__main__":
    #print repeat_length(1, 3)
    #print repeat_length(1, 6)
    #print repeat_length(1, 7)
    #print repeat_length(1, 9)
    max_repeat_len(1000)
