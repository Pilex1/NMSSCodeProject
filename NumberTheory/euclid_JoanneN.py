# Euclidean Algorithm to find gcd

def gcd(a,b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b

a = int(raw_input("What is the larger number? "))
b = int(raw_input("What is the smaller number? "))
gcd = gcd(a,b)
print(gcd)
