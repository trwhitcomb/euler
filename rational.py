
"""
Class for handling rational numbers

"""

def gcd(a, b):
    """
    Use Euclid's algorithm to compute the greatest common divisor of two
    natural numbers.

    """

    if b == 0:
        return a
    else:
        return gcd(b, a % b)
         
    
class Rational(object):

    def __init__(self, numer=None, denom=None):
        if numer is not None and denom is not None:
            self._numer = numer
            self._denom = denom
    
    @staticmethod
    def as_rational(scalar):
        return Rational(scalar, 1)

    @property
    def value(self):
        simplified = self._simplify()
        return (simplified._numer, simplified._denom)

    def __mul__(self, other):
        try:
            result = Rational(self._numer * other._numer,
                              self._denom * other._denom)
        except AttributeError:
            other = Rational.as_rational(other)
            result = Rational(self._numer * other._numer,
                              self._denom * other._denom)
        return result

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        try:
            result_numer = ((self._numer*other._denom) + 
                            (other._numer*self._denom))
            result_denom = self._denom * other._denom
        except AttributeError:
            other        = Rational.as_rational(other)
            result_numer = ((self._numer*other._denom) + 
                            (other._numer*self._denom))
            result_denom = self._denom * other._denom
        return Rational(result_numer, result_denom) 

    def __radd__(self, other):
        return self.__add__(other)
        
    def _simplify(self):
        common_factor = gcd(self._numer, self._denom)
        return Rational(self._numer / common_factor,
                        self._denom / common_factor)

    def __repr__(self):
        return (self._numer, self._denom) 

# Long division algorithm

import itertools

def divide(a, b):
    q = a / b
    r = a - (q * b)
    return q, r

def generate_digits(original_value):
    """
    Given an integer value, returns the values of each digit in sequence,
    followed by a sequence of zeroes.  A None value in the stream signifies
    the end of the original digits
    """
    value_digits = (int(d) for d in str(original_value))
    all_zeroes   = itertools.repeat(0)
    return itertools.chain(value_digits, all_zeroes)

def quotient_stream(a, b):
    r = 0
    for next_digit in generate_digits(a):
        r = r*10 + next_digit
        if r == 0:
            raise StopIteration
        q, r = divide(r, b)
        yield q

def repeat_length(a, b):
    """
    Return the length of the repeating portion of the decimal representation
    of a / b.  Returns zero if the decimal terminates.

    """
    digits   = list()
    quotient = quotient_stream(a, b)
    print '*', a, b
    all_zero = True
    try:
        while True:
            next_digit = quotient.next()
            if all_zero and next_digit != 0:
                all_zero = False
            if not all_zero:
                print next_digit, digits
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
    #print trials[l.index(max_value)]
    print zip(trials, l)

if __name__ == "__main__":
    max_repeat_len(1000)
