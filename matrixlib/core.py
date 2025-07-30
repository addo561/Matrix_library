# Matrix class and basic operations
# focuses on 1d,2d
from typing_extensions import List,Tuple


class MatrixCreation:
    @staticmethod
    def matrix_2d(inputs: List|Tuple,Type:str):
        if type(inputs) == tuple and  Type == '1s':
            L =  [ 1 for _ in  range(inputs[1]) for _ in  range(inputs[0])]
            return  L
        return  inputs


    @staticmethod
    def matrix_1d(t_L:List|int,Type:str):
        #for ones
        if type(t_L)==int and Type == '1s':
            L =  [1 for _ in range(t_L)]
            return L
        return t_L

    @staticmethod
    def zeros():
        pass

    @staticmethod
    def ones(n1=None,n2=None):
        #takes input  as two integers
        ones = []
        if n1:
            ones = MatrixCreation.matrix_1d(n1,Type='1s')# 1 for ones
        elif  n1 and n2 :
            ones =  MatrixCreation.matrix_2d((n1,n2),Type='1s')
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

m = MatrixCreation.ones()
print(m)
