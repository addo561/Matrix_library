# Matrix class and basic operations
# focuses on 1d,2d
from typing_extensions import List,Tuple


class MatrixCreation:
    @staticmethod
    def matrix_2d(inputs: List|int):
        pass

    @staticmethod
    def matrix_1d(t_L:List|int):
        if type(t_L)==int:
            L =  [0 for _ in range(t_L)]
            return L
        return t_L

    @staticmethod
    def zeros():
        pass

    @staticmethod
    def ones(n1=None,n2=None):
        #takes input  as two integera
        ones = []
        if n1:
            ones = MatrixCreation.matrix_1d(n1)
        elif n2:
            ones = MatrixCreation.matrix_1d(n2)
        elif not  n1 and n2 :
            ones =  MatrixCreation.matrix_2d(n1,n2)
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
