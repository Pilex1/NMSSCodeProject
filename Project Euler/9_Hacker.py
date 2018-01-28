def gcd(a,b):
    while a%b!=0: a,b=a%b,a
    return b
def pythags(n):
    if n%2==1: return
    n//=2
    for u in range(int(n**(1/2))+1):
        for v in range(1,u):
            if (n%(u*(u+v))==0 and gcd(u,v)==1 and (u*v)%2==0):
                print((u**4-v**4)*2*u*v*(n//(u*(u+v)))**3)#professional hacking
pythags(1000)
