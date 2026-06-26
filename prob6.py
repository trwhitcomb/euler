#!/usr/bin/env python

numbers = [i+1 for i in range(100)]

sum_squares = sum([n*n for n in numbers])
square_sum = sum(numbers) * sum(numbers)

print(sum_squares - square_sum)