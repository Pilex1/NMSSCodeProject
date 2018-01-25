"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

primes = [2]

n = 3
while len(primes) < 10001:
    isPrime = True
    for p in primes:
        if n % p == 0:
            isPrime = False

    if isPrime:
        primes.append(n)
        print n

    n+=1

print primes[-1]