"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

Joanne I used your code I just fixed up some loops and added some prints to make it work with the big number. I didn't
want to just commit over your thing, but I consider this code yours...
"""

x = 600851475143
primef = []

def isPrime(n):

    a = 2
    while (a <= n**1/2):
        if n % a == 0:
            return False
        else:
            return True
        a += 1
    return False

n = 2
while (n <= x**1/2):
    isPrime(n)
    if (isPrime(n)):
        if x % n == 0:
            primef.append(n)
            print(n)

    n += 1

print(primef[-1])

import time
start_time = time.clock()
isPrime(n)
print time.clock() - start_time, "seconds"