"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

def isPrime(n):
    for a in range (2,(n**1/2+1)):
        if n % a == 0:
            return False
    else:
        return True

p = 0
for n in range(2,2000000):
    if isPrime(n) == True:
        p = p + n
        print(p)
