##TEST CHANGE

### PROBLEM 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

## BASE EXAMPLE
counter=0
for i in range(1,10):
    if (i % 3 == 0) or (i % 5 == 0):
        counter=counter+i
print(counter)

## ACTUAL PROBLEM
counter1 = 0
for a in range(1,1000):
    if (a % 3 == 0) or (a % 5 == 0):
        counter1 = counter1 + a
print(counter1)

## ALTERNATE SOLUTION
counter1 = 0
b=1
for a in range(1,1000):
    if (b % 3 == 0) or (b % 5 == 0):
        counter1 = counter1 + a
    b=b+1
print(counter1)

"""
THis entire thing is a comment
"""
