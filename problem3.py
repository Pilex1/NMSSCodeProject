"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""


x = 13195
primef = []

def isPrime(n):
    for a in range (2,n**1/2):
        if n % a == 0:
            return False
    else:
        return True

for n in range (2,x**1/2):
    isPrime(n)
    if (isPrime(n)==True):
        if x % n == 0:
            primef.append(n)

print(primef[-1])

import time
start_time = time.clock()
isPrime(n)
print time.clock() - start_time, "seconds"

"""
## Try finding factors first and then finding which factors are primes
x = 13195
factors = []
pfactors = []

def factor(x):
    for a in range(1,x+1):
        if x % a == 0:
            factors.append(a)
    print(factors)

factor(x)

def prime(x):
    for a in range(2,x**1/2):
        if x % a != 0:
            return True

print(prime(x))

print(pfactors)
"""
