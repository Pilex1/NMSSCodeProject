__author__ = 'My Computer'
#start: 10:10



#uses a local file I made with comma separated primes up to 29999999
primes = list(map(int,open("primes").read().split(",")[:-1]))


#returns a tuple of numbers to check through
'''
used similarly to range(x)
eg:
for e in gen(11):
    print(e)

output:
    (5,6)               (from yield(a,x-a))
    (6,5)               (from yield(x-a,a))
    (4,7)               (from yield(a,x-a))
    (7,4)               (from yield(x-a,a))
    (3,8)               (etc.)
    (8,3)
    (2,9)
    (9,2)
    (1,10)
    (10,1)
'''
def gen(x):
    a = x//2
    if(x == 2):
        yield (a,a)
        a=0
    while(a!=0):
        if(x%a != 0):
            yield (a,x-a)
            yield (x-a,a)
        a-=1


#Question answer function
def F(x):
    #number of gridpoints touched
    n = 0

    #size will be decomposed as all possible sums of two coprime numbers, and these pairs will be repeatedly subtracted from x until x is the smallest positive integer possible
    size = 1
    while True:
        size += 1
        cycles = eulerTotient(size)#counts the number of coprime pairs
        n+=cycles
        x-=cycles*size//2 #cycles//2 is number of pairs
        if(x<=0):
            n-=cycles
            x+=cycles*size//2
            y = x
            for i in gen(size): #gen(size) outputs coprime pairs that sum to size
                n+=1
                x-=i[1]
                y-=i[0]
                if(x<0 or y<0):
                    #print("answer",n)
                    return n



#returns set of prime factors
def getPrimeFactors(num):
    factors = []
    for p in primes:
        val = num//p
        if(val*p == num):
            factors.append(p)
            val = num//p
        while val*p == num:
            num = val
            val = num//p
        if p*p > num: break
    if num != 1:
        factors.append(num)
    return factors

#gets quantity of numbers less than num comprime to num
#try to prove this first!!
def eulerTotient(num):
    out = num
    for p in getPrimeFactors(num):
        out*=p-1
        out//=p
    return out



print(F(10**18))







