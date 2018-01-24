# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 09:52:56 2018

@author: jwright.06
"""
a = 0
b = 0
Solved = False
Solved1 = False

while Solved == False:
    a += 1
    b = 0
    while Solved1 == False and b + a <= 1000:
        if a**2 + b**2 == (1000-(a+b))**2:
            Solved  = True
            Solved1 = True
        else:
            b += 1
            
result  = a*b*(1000 - a - b)
print(result)