"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import time

def isPalindrome(n):
    m = int(str(n)[::-1])
    if n == m:
        return True
    else:
        return False

def largestIn(array):
    largest = 0
    for i in array:
        if i > largest:
            largest = i

    return largest

def largestPalindromeProduct3():

    dromes = []

    for i in range(100, 1000):
        for j in range(100, 1000):
            if isPalindrome(i*j):
                dromes.append(i*j)

    return largestIn(dromes)

startTime = time.clock()
p = largestPalindromeProduct3()
print(p)
print "took", time.clock() - startTime, "seconds"
