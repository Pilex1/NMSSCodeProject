__author__ = 'My Computer'
import math
class APFloat:
    "Stores a float as two integers, value is num * (2**exp)"
    #integers
    exp = 0
    num = 0

    maxprecision = 0

    def __init__(self,num,exp = None,precision:int = 2**64):
        """
        int,int
        float
        int
        """

        self.maxprecision = precision
        #one parameter is given
        if(not exp):
            #case float
            #floats have 53 bits of precision
            if(isinstance(num,float)):
                self.exp = int(math.log2(abs(a)))-53
                self.num = int(num/2**self.exp)
                return
            #case int is given
            if(isinstance(num,int)):
                self.num = num
                self.exp = 0
                return
        else:
            self.exp = exp
            self.num = num
    def __mul__(self, other):
        out = APFloat(self.num*other.num,self.exp+other.exp)
        out.ensurePrecision()
        return out
    def __div__(self, other):


    def __gt__(self, other):
        selfsign = self.num>0
        othersign = self.num>0
        #both positive
        if(selfsign and othersign):
            if(self.exp >other.exp):
                return self
            elif(self.exp == other.exp):

        elif(selfsign):
            return self
        elif(othersign):
            return other
        #both negative
        else:
            if(self.exp<other.exp):




        if(self.exp == other.exp):
            s

        self.exp>other.exp):
            return self

        e


    def ensurePrecision(self):
        while(abs(self.num)>self.maxprecision):
            self.num//=2
            self.exp+=1
        while(abs(self.num)<self.maxprecision):
            self.num*=2
            self.exp-=1



if __name__ == "__main__":
    a = -0.00141234
    exp = int(math.log2(abs(a)))-53
    print(a//2**exp)
