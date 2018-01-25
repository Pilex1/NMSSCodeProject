"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.
What is the 10 001st prime number?
"""

primes = []

def isPrime(n):
    for a in range (2,(n**1/2+1)):
        if n % a == 0:
            return False
    else:
        return True

def prime_generator():
    n = 2
    while len(primes) < 10001:
        if isPrime(n) == True:
            primes.append(n)
        n = n + 1
    return primes[-1]

print(prime_generator())
