__author__ = 'My Computer'
import math
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
        if(type(num) == APFloat):
            self.num = num.num
            self.maxprecision = num.maxprecision
            self.exponent = num.exponent
            print("copy")
            return
        self.maxprecision = precision
        #one parameter is given
        if(not exp):
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
                self.exponent = 0
                self.__ensurePrecision()
                return
        else:
            self.exponent = exp
            self.num = num
            self.__ensurePrecision()

    def __mul__(self, other):
        if(type(other)!=APFloat):
            other = APFloat(other)
        maxprecision = min(self.maxprecision,other.maxprecision)
        out = APFloat(self.num*other.num,self.exponent+other.exponent,maxprecision)
        out.__ensurePrecision()
        return out
    def __truediv__(self, other):
        if(type(other)!=APFloat):
            other = APFloat(other)
        maxprecision = min(self.maxprecision,other.maxprecision)
        maxval = min(self.maxval,other.maxval)
        out = APFloat(self.num*maxval
                      //(other.num), self.exponent-other.exponent-maxprecision,maxprecision)
        out.__ensurePrecision()

        return out

    #The lower exponent wins, lower precision wins
    def __add__(self, other):
        if(type(other)!=APFloat):
            other = APFloat(other)
        precision = min(self.maxprecision,other.maxprecision)
        exp = max(self.exponent,other.exponent)
        num = self.num // 2**(exp-self.exponent)+other.num // 2**(exp-other.exponent)
        out = APFloat(num,exp,precision)
        out.__ensurePrecision()
        return out
    def __sub__(self, other):
        if(type(other)!=APFloat):
            other = APFloat(other)
        precision = min(self.maxprecision,other.maxprecision)
        exp = max(self.exponent,other.exponent)
        num = self.num // 2**(exp-self.exponent)-other.num // 2**(exp-other.exponent)
        out = APFloat(num,exp,precision)
        out.__ensurePrecision()
        return out
    def __neg__(self):
        out = APFloat(self)
        out.num *=-1
        return out
    def __str__(self):
        return "{}".format(float(self))
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
        print((self-other).num)
        if(self - other):
            return False
        return True
    def __ensurePrecision(self):
        if(self.num == 0): return
        while(abs(self.num)>self.maxval):
            self.num//=2
            self.exponent+=1
            #print("high",self.num)
        while(abs(self.num)<self.maxval):
            self.num*=2
            self.exponent-=1
            #print("low")
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
        result = APFloat(self)
    def reciprocal(self):
        return APFloat(1,precision=self.maxprecision)/self

    def exp(self):
        i = 1
        out = APFloat(0,precision = self.maxprecision)
        term = APFloat(1,precision = self.maxprecision)
        while(True):
            old = APFloat(out)
            print(term)
            out += term
            print(out-old)

            if(out == old): return out

            term *= self/i
            i+=1

    def ln(self):
        #newton's method
        x0 = APFloat(self)
        for i in range(100):
            x0 += x0.exp().reciprocal()*self -1
        return x0

    @property
    def maxprecision(self):
        return self.__maxprecision
    @maxprecision.setter
    def maxprecision(self,val:int):
        print("setPrecision",val)
        if(type(val)!=int):
            print("val expected int, got " + str(type(val)))
        self.__maxprecision = val
        self.maxval = 2**val






if __name__ == "__main__":
    a,b,c,d = 100,3,20,3

    f = APFloat(a,c,1000)
    f1 = APFloat(b,d,100)
    print("f1",f1)
    print("f",f)
    print("+",f+f1)
    print(float((a*2**c+b*2**d)))
    print("*",f*f1)
    print(float((a*2**c*b*2**d)))
    print("/",f/f1)
    print(float(((a*2**c)/(b*2**d))))
    print(">",f>f1)
    print((a*2**c)>(b*2**d))
    print("<",f<f1)
    print((a*2**c)<(b*2**d))
    print("==",f==f1)
    print((a*2**c)==(b*2**d))
    print(f1.exp(),"exp")
    print(math.exp(b*2**d))
    print(f1.ln(),"ln")
    print(math.log(b*2**d))

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






