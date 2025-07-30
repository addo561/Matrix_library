# Matrix class and basic operations
# focuses on 1d,2d
from typing_extensions import List,Tuple


class MatrixCreation:
    @staticmethod
    def matrix_2d(inputs: List|Tuple,Type:str):
        if type(inputs) == tuple and  Type == 'O':



    @staticmethod
    def matrix_1d(t_L:List|int,Type:str):
        #for zeros
        if type(t_L)==int and Type == 'O':
            L =  [0 for _ in range(t_L)]
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
            ones = MatrixCreation.matrix_1d(n1,Type='O')# O for ones
        elif  n1 and n2 :
            ones =  MatrixCreation.matrix_2d((n1,n2),Type='O')
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
