# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:30:38 2018

@author: jwright.06
"""

a = 9973
primes = []

def prime_generator():
    a = 2
    
    while len(primes) <= 10002:
        prime = True
        
        for x in primes:
            if a%x == 0:
                prime = False
            
        if prime == True:
            primes.append(a)
            f = len(primes)
            print(a)
            print('-')
            print(f)
            
        a += 1
    
    return primes
        
r = prime_generator()
a = r[10002]
print('done')
print(a)