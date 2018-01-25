"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers
is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
ANSWER: 906609
"""

palprod = []

def pal (x,y):
    digits = []
    z = x * y
    a = len(str(z))
    for n in range (1,a+1):
        d = 0
        while (z - 10**(a-n) >= 0):
            z = z - 10**(a-n)
            d = d + 1
        digits.append(d)
    for n in range (1,a+1):    ###HELP when I try to make this miore concise.
        if (digits[0] == digits[-1]):    ###the code doesn't work
            if (digits[1] == digits[-2]):
                if (digits[2] == digits[-3]):
                    return True
        return False

for a in range (900,1000):
    for b in range (900,1000):
        if pal (a,b) == True:
            palprod.append(a*b)

print(palprod[-1])
