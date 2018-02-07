__author__ = 'My Computer'
#currently limited to 2D matrices, nD tensors are wtf
# In theory a incompatblesize error should be defined for operations like a*b , but ill do it later

class Matrix:



    # data: numbers
    # dim: dimensions x,y
    # filler: default value
    # repeat: 1,2,0,0... vs 1,2,1,2,1,2...

    def __init__(self, data, dim:tuple = (1,1), filler = 0, repeat = False):

        # list of lists
        self.data = []

        # if data is a 2D list
        # if your matrix is filled with potato objects you're an idiot and should be ashamed of yourself.
        # if your potato has notions of commutative addition and multiplication I might forgive you
        if(isinstance(data,list) and isinstance(data[0],list)):
            self.data = data
            if(not self.__isRectangular()):
                print("2d list provided is not rectangular")
                self.data = []
            return

        # if data is a scalar, fill the entire matrix with that number using code below
        if(isinstance(data,(int,float,complex))):
            data = [data]
            repeat = True

        # data = 1D list, dim = (x,y) : places the elements of data into an x*y matrix, filling row by row.
        # Excess elements are ignored, filler is used when data runs out of elements. Filler is 0 by default
        if(isinstance(data,list) and isinstance(dim,tuple)):
            i = 0
            for y in range(dim[1]):
                row = []
                for x in range(dim[0]):
                    if(i>=len(data) and repeat): i = 0 # if repeat is true cause i to loop
                    row.append(data[i] if i<len(data) else filler)
                    i+=1
                self.data.append(row)
            return




    def __str__(self):
        out = ""
        for row in self.data:
            out +=str(row)+"\n"
        return out

    # self + other : define for matrices, scalars
    def __add__(self,other):
        pass
    # say we had int - matrix: since int has no definition of having matrices subtracted from it, the expression will fail.
    # Python wll then try to call reverse sub or __rsub__ for matrix, reversing the parameters. (see __rsub__ below)
    def __radd__(self,other):
        return self+other


    def __sub__(self, other):
        pass
    def __rsub__(self, other):
        return -(self-other)

    # define for matrices and scalars
    def __mul__(self,other):
        pass


    # apply |x| to all elements x
    def __abs__(self):
        pass

    # apply -x to all elements x
    def __neg__(self):
        pass

    # gorssian eliminaton
    # am aware nonsquare matrices dont have explicit inverse.
    def inverse(self):
        pass

    # dont know how I would implement this myself
    #iverses for nonsquare matrices. Square matrices should get the same result for leftinverse() ,rightinverse() and inverse()
    def rightinverse(self):
        pass

    def leftinverse(self):
        pass


    def transpose(self):
        pass

    def det(self):
        pass

    #returns list of eigenvalues
    def eigenvalues(self):
        pass

    #returns list of eigenvectors and eigenvalues
    def eigenvectors(self):
        pass












    # ensuring that no shenanegans are going on with matrix size
    def __isRectangular(self):
        for row in self.data:
            if(len(row)!=len(self.data[0])):
                return False
        return True





if __name__ == "__main__":
    m1 = Matrix(1,(3,4))
    print(m1)
    m2 = Matrix([1,2,3],(4,3))
    print(m2)
    m3 = Matrix([1,2,3],(4,3),repeat = True)
    print(m3)
    m4 = Matrix([[1,2,3],[6,5,4],[11,12,13]])
    print(m4)
    m5 = Matrix([1,2],(3,3),filler = 3)
    print(m5)







