import mpmath
# you need to install the mpmath library: in cmd: pip3 install mpmath

# decimal points of precision
mpmath.dps = 1000

# x - the number to calculate the expansion of
# n - number of terms in expansion
def continued(x, n):
    l = []
    q = mpmath.floor(x)
    for i in range(n-1):
        # x = bq + r
        b = mpmath.floor(x/q)
        l.append(b)
        r = x - b*q
        x, q = q, r
    return l

# eg. calculates the expansion of sqrt3
for i in continued(3**0.5,20):
    print(i)