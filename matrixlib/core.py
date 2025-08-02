# Matrix class and basic operations
# focuses on 1d,2d
from typing import List,Tuple
from typing import Union
import  random


class MatrixCreation:
    @staticmethod
    def matrix_2d(inputs: Union[List,Tuple],function=None,fill=None):
        if isinstance(inputs,tuple):
            if fill is not None and function is None:
                return [ [fill for _ in  range(inputs[1])] for _ in  range(inputs[0])] #zeros and ones

            if  function =='normal':
                if inputs[0]<0 or inputs[1]<0:
                    raise ValueError('dimensions must be positive')
                if  fill:
                    L =  [ [0 for _ in  range(inputs[1])] for _ in  range(inputs[0])]
                    idx =  0
                    for i in range(len(L)):
                        for j in range(len(L[0])):
                                L[i][j] = fill[idx]
                                idx += 1
                    return L
            if function  ==  'I':
                if inputs[0]<0 or inputs[1]<0:
                    raise ValueError('dimensions must be positive')
                matrix  = [ [0 for _ in  range(inputs[1])] for _ in  range(inputs[0])]
                for i in range(inputs[0]):
                    for j  in range(inputs[1]):
                        if i ==j:
                            matrix[i][j]=1
                return matrix

        if  isinstance(inputs,list) :
            if  not inputs:
                raise ValueError('Empty list')
            if not isinstance(inputs[0],list):
                 raise ValueError('Expected 2D ')
            return inputs
        else:
            raise TypeError(f'Expected list but got {type(inputs).__name__}')


    @staticmethod
    def matrix_1d(t_L:Union[List,int],fill=None):
        #for ones and  zeros
        if isinstance(t_L,int) :
            if fill:
                L =  [fill for _ in range(t_L)]
                return L
        elif isinstance(t_L,list):
            if not t_L:
                raise ValueError('Empty  List  is not a valid 1D')
            elif  isinstance(t_L[0],list) and  fill is None:
                raise ValueError('Expected 1D ')
            return t_L
        raise TypeError(f'Expected list but got {type(t_L).__name__}')


    @staticmethod
    def zeros(n1=None,n2=None):
        #takes input  as two integers
        if n1 is None: #none case
            raise ValueError('at least 1 dimensions must be provided')
        if n2 is None:# 1D case
            zeros = MatrixCreation.matrix_1d(n1,fill=0)
        else:
            zeros =  MatrixCreation.matrix_2d((n1,n2),fill=0) # 2d case
        return  zeros

    @staticmethod
    def ones(n1=None,n2=None):
        #takes input  as two integers
        if n1 is None: #none case
            raise ValueError('at least 1 dimensions must be provided')
        if n2 is None:# 1D case
            ones = MatrixCreation.matrix_1d(n1,fill=1)# 1 for ones
        else:
            ones =  MatrixCreation.matrix_2d((n1,n2),fill=1) # 2d case
        return  ones

    @staticmethod
    def Identity(x,y):
        if x<0 or y<0:
            raise ValueError('dimensions must be positive')
        I = MatrixCreation.matrix_2d((x,y),function='I',fill=None)
        return I



    @staticmethod
    def normal(low,high,size:Tuple):
        if type(size) is not tuple:
            raise TypeError('size must be  a tuple')
        assert low < high ,f'lower bound greater than high,  fix ({low,high})'
        normal = []
        if len(size) == 1:
            normal = [random.uniform(low,high) for i in range(size[0])]
        else:
            normal = MatrixCreation.matrix_2d(size,function='normal',fill=[random.uniform(low,high) for _ in range(size[0]*size[1])])
        return  normal


    @staticmethod
    def randint(x,y):
        if x > y:
            raise ValueError('lower bound must be lesser than  upper bound')
        return random.randint(x,y)

#just for checking  whiles coding,wrote  tests  later
m = MatrixCreation.ones(3,2)
print(m)
