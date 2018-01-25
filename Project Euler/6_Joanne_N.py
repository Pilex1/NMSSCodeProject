"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""
n = 100

def sum_of_squares():
    x = 1
    y = 0
    while x < (n+1):
        y = y + x**2
        x = x + 1
    return y

def square_of_sum():
    x = 1
    y = 0
    while x < (n+1):
        y = y + x
        x = x + 1
    y = y ** 2
    return y

difference = int(square_of_sum()) - int(sum_of_squares())
print(difference)
