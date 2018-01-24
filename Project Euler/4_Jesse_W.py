# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 17:14:42 2018

@author: jwright.06
"""

#returns True if input number is palendrome
def palendrome(num):
    a = str(num)
    palendrome = True
    for x in range (0, len(a)):
        if a[x] != a[len(a) - 1 - x]:
            palendrome = False
    return palendrome
greatest = 0
for x in range(100,999):
    for y in range(100,999):
        if palendrome(x*y) == True and x*y > greatest:
            greatest  = x*y
        
print(greatest)
