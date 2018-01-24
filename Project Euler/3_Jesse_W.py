# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:30:38 2018

@author: jwright.06
"""

l = 0
primes = []
prime = False


def prime_generator(start, stop):
    a = start
    l = 0
    while a <= stop:
        prime = True
        
        for x in primes:
            if a%x == 0:
                prime = False
            
        if prime == True:
            primes.append(a)
            print(a)
            l = l + a
            
        a += 1
    
    return primes
        
x = prime_generator(2,2*(10**6))
print('done')
print(l)

