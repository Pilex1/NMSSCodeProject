__author__ = 'My Computer'
import math
import sys
class APFloat:
    "Stores a float as two integers, value is num * (2**exp)"
    #integers
    exponent = 0
    num = 0

    maxval = 0
    __maxprecision = 0

    def __init__(self,num,exp = None,precision:int = 64):
        """
        int,int
        float
        int
        """
        if(isinstance(num,APFloat)):
            self.num = num.num
            self.maxprecision = num.maxprecision
            self.exponent = num.exponent
            print("copy")
            return
        self.maxprecision = precision
        #one parameter is given
        if(exp==None):
            #case float
            #floats have 53 bits of precision
            if(isinstance(num,float)):
                self.exponent = int(math.log2(abs(num)))-53
                self.num = int(num/2**self.exponent)
                self.__ensurePrecision()
                return
            #case int is given
            if(isinstance(num,int)):
                self.num = num
                if(num == 0):
                    self.exponent = -float("inf")
                    self.maxprecision = float("inf")
                    return
                self.exponent = 0

                self.maxprecision = float("inf")
                return
        else:
            self.exponent = exp
            self.num = int(num)
            self.__ensurePrecision()
    def __rmul__(self, other):
        return self*other
    def __mul__(self, other):
        if(type(other) == int):
            out = APFloat(self.num*other,self.exponent,self.maxprecision)
        else:
            if(type(other)!=APFloat):
                other = APFloat(other)
            maxprecision = min(self.maxprecision,other.maxprecision)
            out = APFloat(self.num*other.num,self.exponent+other.exponent,maxprecision)
        return out
    def __rtruediv__(self, other):
        return APFloat(other)/self
    def __truediv__(self, other):
        if(type(other)!=APFloat):
            other = APFloat(other)
        maxprecision = min(self.maxprecision,other.maxprecision)
        maxval = min(self.maxval,other.maxval)
        out = APFloat(self.num*maxval
                      //(other.num), self.exponent-other.exponent-maxprecision,maxprecision)

        return out

    #The lower exponent wins, lower precision wins
    def __radd__(self, other):
        return self+other
    def __add__(self, other:(int,float)):
        if(type(other)!=APFloat):
            other = APFloat(other)

        precision = min(self.maxprecision,other.maxprecision)
        exp = max(self.exponent,other.exponent)
        num = self.num // 2**(exp-self.exponent)+other.num // 2**(exp-other.exponent)
        out = APFloat(num,exp,precision)
        return out
    def __rsub__(self,other):
        return APFloat(other)-self
    def __sub__(self, other):
        if(type(other)!=APFloat):
            other = APFloat(other)
        precision = min(self.maxprecision,other.maxprecision)
        exp = max(self.exponent,other.exponent)
        num = self.num // 2**(exp-self.exponent)-other.num // 2**(exp-other.exponent)
        out = APFloat(num,exp,precision)
        return out
    def __neg__(self):
        out = APFloat(self)
        out.num *=-1
        return out
    def __str__(self):
        try:
            return "{}".format(float(self))
        except(OverflowError):
            return "{}*2**{}".format(self.num,self.exponent)
    #gt -> self > other
    #self < other is by default implemented by calling other > self
    def __gt__(self, other):
        if(type(other)!=APFloat):
            other = APFloat(other)
        selfsign = self.num>0
        othersign = self.num>0
        selfexp = self.exponent+self.maxprecision
        otherexp = other.exponent+other.maxprecision
        #both positive
        if(selfsign and othersign):
            if(selfexp>otherexp):
                return True
            elif(selfexp == otherexp):
                return self.num>other.num
            return False

        elif(selfsign):
            return True
        elif(othersign):
            return False
        #both negative
        else:
            if(selfsign and othersign):
                if(selfexp <otherexp):
                    return True
                elif(selfexp == otherexp):
                    return self.num<other.num
            return False
    #self == other
    def __lt__(self, other):
        if(type(other)!=APFloat):
            other = APFloat(other)
        selfsign = self.num>0
        othersign = self.num>0
        selfexp = self.exponent+self.maxprecision
        otherexp = other.exponent+other.maxprecision
        #both positive
        if(selfsign and othersign):
            if(selfexp<otherexp):
                return True
            elif(selfexp == otherexp):
                return self.num<other.num
            return False

        elif(selfsign):
            return True
        elif(othersign):
            return False
        #both negative
        else:
            if(selfsign and othersign):
                if(selfexp >otherexp):
                    return True
                elif(selfexp == otherexp):
                    return self.num>other.num
            return False

    def __eq__(self, other):
        if(type(other)!=APFloat):
            if(type(other) in (int,float,complex)):
                other = APFloat(other)
            else:
                return False
        if(self.num == other.num and self.exponent == other.exponent and self.__maxprecision == other.__maxprecision):
            return True
        return False
    def __ensurePrecision(self):

        oldexp = self.exponent
        if(self.num == 0):
            self.exponent = -float("inf")
            return
        if(self.maxprecision == float("inf")):
            return
        t = time.time()
        p = self.__maxprecision
        siz = sys.getsizeof(self.num)

        offset = ((siz-28)//4)*30 - p
        t = time.time()-t
        #if(t>0):
            #print("ensure took: ",t,"seconds with",oldexp,"->",self.exponent)
            #print("siz:",siz,"offset:",offset)
        if(offset>0):
            self.num>>=offset #divide by 2**offset
            self.exponent+=offset
        if(offset<0):
            self.num<<=-offset #multiply by 2**offset
            self.exponent+=offset
        offset2 = int(math.ceil(math.log2(abs(self.num)) - self.maxprecision))
        self.num>>=offset2
        self.exponent += offset2
        pass



    def __float__(self):
        return float(self.num*2**(self.exponent))
    def __int__(self):
        if(self.exponent>=0):
            return
    def __bool__(self):
        return self.num != 0
    def __abs__(self):
        out = APFloat(self)
        out.num = abs(out.num)
        return out
    def __pow__(self, power, modulo=None):
        print("problem too hard")
        return 10
    def sqrt(self):
        result = APFloat(self/2)

        while (True):
            oldresult = result
            result = result/2 + self/(2*result)
            if (result == oldresult):
                return result


    def reciprocal(self):
        return APFloat(1,precision=self.maxprecision)/self

    def exp(self):
        i = 1
        out = APFloat(0,precision = self.maxprecision)
        term = APFloat(1,precision = self.maxprecision)
        while(True):
            old = out
            out += term
            if(out == old): return out
            term *= self/i
            i+=1

    def ln(self):
        #newton's method
        '''
        x0 = APFloat(self)
        for i in range(100):
            x0 += x0.exp().reciprocal()*self -1
        return x0
        '''
        #print("self",self)
        x = (self-1)/(self+1)
        #calculates ln(1+x/1-x) = 2*(x + x^3/3 + x^5/5 + x^7/7 + ...)
        term = APFloat(2*x)
        x2 = x*x #x^2
        out = APFloat(0)
        i = 1
        while (True):
            old = out
            out += term/i
            if(old == out): return out
            term *= x2 # x, x^3, x^5, x^7....
            i += 2     # 1, 3  , 5  , 7  ....

    @property
    def maxprecision(self):

        return self.__maxprecision
    @maxprecision.setter
    def maxprecision(self,val:int):
        #print("setPrecision",val)
        if(type(val)!=int and val != float("inf")):
            print("val expected int, got " + str(type(val)))
        self.__maxprecision = val
        self.maxval = 2**val






if __name__ == "__main__":
    import time

    a,b,c,d = 100,34,-20,-3

    f = APFloat(a,c,500)
    f1 = APFloat(b,d,500)
    print("f1",f1,b*2**d)
    print("f",f,a*2**c)
    print("+",f+f1)
    print(float((a*2**c+b*2**d)))
    t = time.time()
    x = f1*f
    t = time.time()-t

    print(x,"*",t)
    t = time.time()
    x = (a*2**c) * (b*2**d)
    t = time.time()-t

    print(x,t)

    print("/",f/f1)
    print(float(((a*2**c)/(b*2**d))))
    print(">",f>f1)
    print((a*2**c)>(b*2**d))
    print("<",f<f1)
    print((a*2**c)<(b*2**d))
    print("==",f==f1)
    print((a*2**c)==(b*2**d))
    print("+",1+f1)
    print(1+(b*2**d))
    print("==",1/f1)
    print(1/(b*2**d))
    print("==",f==f1)
    print((a*2**c)==(b*2**d))


    t = time.time()
    x = f1.exp()
    t = time.time()-t

    print(x,"exp",t)
    t = time.time()
    x = math.exp(b*2**d)
    t = time.time()-t


    print(x,"exp",t)

    t = time.time()
    x = f1.ln()
    t = time.time()-t

    print(x,"ln",t)

    t = time.time()
    x = math.log(b*2**d)
    t = time.time()-t
    print(x,"ln",t)

    print("sqrt",f.sqrt())
    print(math.sqrt(a*2**c))



#probably better and faster than int based APFoat
'''
can be thought as a polynomial of 2^53 with floating point coefficients
eg [f1,f2,f3] will be
f1 + 2**53 f2 + (2**53)**2 f3

this way an extra 53 binary digits of precision can be gained per term
'''
'''
precision rules:
a*b: lowest precision is inherited
a+b: lowest precision is inherited
a/b: lowest precision is inherited



'''
class APFloat1:
    #array of floats
    nums = [0]

    def __init__(self,*floats):
        pass






