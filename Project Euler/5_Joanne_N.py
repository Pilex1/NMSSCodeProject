"""
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

def gcd(a,b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b

def div():
    x = 2
    y = 3
    while y < 21:
        if gcd(x,y) == 1:
            x = x * y
            y = y + 1
        if gcd(x,y) != 1:
            x = x * y/gcd(x,y)
            y = y + 1
    return x

p = div()
print(p)
