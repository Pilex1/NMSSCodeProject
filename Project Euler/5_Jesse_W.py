# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 20:22:18 2018

@author: jwright.06
"""
a = 0
b = 0
for x in range(1,101):
    a += x**2
    b += x
    

c = b**2 - a
print(c)