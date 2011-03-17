
"""
Class for testing rational number handling

"""

import unittest

from rational import Rational, gcd

class TestEuclid(unittest.TestCase):
    def testGcd(self):
        """Check GCD algorithm"""
        self.assertEquals(gcd(5, 3), 1)
        self.assertEquals(gcd(6, 3), 3)
        self.assertEquals(gcd(21, 14), 7)

class TestRational(unittest.TestCase):
    def testInit(self):
        """Initialize a rational number."""
        r = Rational(5, 7)
        self.assertEquals(r._numer, 5)
        self.assertEquals(r._denom, 7)

    def testScalar(self):
        """Initialize a rational number using a scalar."""
        r = Rational.as_rational(12)
        self.assertEquals(r._numer, 12)
        self.assertEquals(r._denom, 1)

    def testRationalMultiply(self):
        """Multiply two rational numbers."""
        a = Rational(5, 7)
        b = Rational(2, 3)
        c = a * b
        self.assertEquals(c._numer, 10)
        self.assertEquals(c._denom, 21)

    def testScalarMultiply(self):
        """Multiply a rational number by a scalar."""
        a = Rational(5, 7)
        b = 12
        c = a * b
        self.assertEquals(c._numer, 60)
        self.assertEquals(c._denom, 7)

    def testScalarRMultiply(self):
        """Multiply a scalar by a rational number."""
        a = Rational(5, 7)
        b = 12
        c = b * a
        self.assertEquals(c._numer, 60)
        self.assertEquals(c._denom, 7)

    def testRationalAdd(self):
        """Add two rational numbers."""
        a = Rational(5, 7)
        b = Rational(2, 3)
        c = a + b
        self.assertEquals(c._numer, 29)
        self.assertEquals(c._denom, 21)

    def testScalarAdd(self):
        """Add a rational number and a scalar."""
        a = Rational(5, 7)
        b = 12
        c = a + b
        self.assertEquals(c._numer, 89)
        self.assertEquals(c._denom, 7)

    def testScalarRAdd(self):
        """Add a scalar and a rational number."""
        a = Rational(5, 7)
        b = 12
        c = b + a
        self.assertEquals(c._numer, 89)
        self.assertEquals(c._denom, 7)

    def testSimplify(self):
        """Reduce a rational number to its simplest form."""
        r = Rational(6, 8)
        self.assertEquals(r.value, (3, 4))

from rational import divide, generate_digits, quotient_stream
from rational import repeat_length

class TestDivision(unittest.TestCase):
    def testDigitGenerator(self):
        """Split apart a number into an infinite sequence of digits."""
        gen = generate_digits(23)
        self.assertEquals(gen.next(), 2)
        self.assertEquals(gen.next(), 3)
        self.assertEquals(gen.next(), 0)        

    def testDivide(self):
        """Divide into quotient and remainder."""
        self.assertEquals(divide(5,3), (1, 2))
        self.assertEquals(divide(1,4), (0, 1))

    def testEndlessQuotientStream(self):
        """Check a quotient that goes on forever."""
        q_str = quotient_stream(1, 6)
        self.assertEquals(q_str.next(), 0)
        self.assertEquals(q_str.next(), 1)
        self.assertEquals(q_str.next(), 6)
        self.assertEquals(q_str.next(), 6)
        self.assertEquals(q_str.next(), 6)
        
    def testTerminatingQuotientStream(self):
        """Check a quotient that terminates."""
        q_str = quotient_stream(1, 4)
        self.assertEquals(q_str.next(), 0)
        self.assertEquals(q_str.next(), 2)
        self.assertEquals(q_str.next(), 5)
        self.assertRaises(StopIteration, q_str.next)

    def testRepeatLength(self):
        """Check length of repeating decimal."""
        self.assertEqual(repeat_length(1, 2), 0) 
        self.assertEqual(repeat_length(1, 3), 1) 
        self.assertEqual(repeat_length(1, 4), 0) 
        self.assertEqual(repeat_length(1, 5), 0) 
        self.assertEqual(repeat_length(1, 6), 1) 
        self.assertEqual(repeat_length(1, 7), 6) 
        self.assertEqual(repeat_length(1, 8), 0) 
        self.assertEqual(repeat_length(1, 9), 1) 
        self.assertEqual(repeat_length(1, 10), 0) 
        self.assertEqual(repeat_length(1, 27), 3) 
