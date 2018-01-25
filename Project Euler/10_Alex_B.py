"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

primes = [2]

n = 3
while n < 2000000:
    isPrime = True
    for p in primes:
        if n % p == 0:
            isPrime = False

    if isPrime:
        primes.append(n)
        print n

    n += 1

s = 0
for p in primes:
    s += p

print s
