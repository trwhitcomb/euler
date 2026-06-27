#!/usr/bin/env python

import itertools

for a in range(1000):
    for b in range(a+1,1000):
        for c in range(b+1, 1000):
            if a + b + c == 1000:
                if a*a + b*b == c*c:
                    print(a,b,c)
                    print(a*b*c)