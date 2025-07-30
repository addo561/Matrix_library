# Matrix class and basic operations
# focuses on 1d,2d
from typing_extensions import List,Tuple


class MatrixCreation:
    @staticmethod
    def matrix_2d(inputs: List|Tuple,Type=None):
        if type(inputs) == tuple : #for zeros  and ones
            L =  [ [Type for _ in  range(inputs[1])] for _ in  range(inputs[0])]
            return  L
        return  inputs


    @staticmethod
    def matrix_1d(t_L:List|int,Type=None):
        #for ones and  zeros
        if type(t_L)==int:
            L =  [Type for _ in range(t_L)]
            return L
        return t_L

    @staticmethod
    def zeros(n1=None,n2=None):
        #takes input  as two integers
        zeros = []
        if n1 and not  n2:
            zeros = MatrixCreation.matrix_1d(n1,Type=0)# O for zeros
        elif  n1 and n2 :
            zeros =  MatrixCreation.matrix_2d((n1,n2),Type=0)
        return  zeros

    @staticmethod
    def ones(n1=None,n2=None):
        #takes input  as two integers
        ones = []
        if n1 and not  n2:
            ones = MatrixCreation.matrix_1d(n1,Type=1)# 1 for ones
        elif  n1 and n2 :
            ones =  MatrixCreation.matrix_2d((n1,n2),Type=1)
        return  ones

    @staticmethod
    def Identity():
        pass

    @staticmethod
    def rand():
        pass

    @staticmethod
    def randint():
        pass

#just for checking  whiles coding,wrote  tests  later
m = MatrixCreation.matrix_2d([[1],[2],[3]])
print(m)
