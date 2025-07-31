# Matrix class and basic operations
# focuses on 1d,2d
from typing_extensions import List,Tuple
from typing import Union
import  random


class MatrixCreation:
    @staticmethod
    def matrix_2d(inputs: Union[List,Tuple],function=None,Type=None):

        if  isinstance(inputs,int):
            raise ValueError('must be int form')
        if isinstance(inputs,tuple ) and function is None: #for zeros  and ones
            L =  [ [Type for _ in  range(inputs[1])] for _ in  range(inputs[0])]
            return  L

        if  function =='normal':
            if not isinstance(inputs,tuple) :
                raise ValueError('must be a tuple')
            if inputs[0]<0 or inputs[1]<0:
                raise ValueError('dimensions must be positive')
            L =  [ [0 for _ in  range(inputs[1])] for _ in  range(inputs[0])]
            if Type:
                idx =  0
                for i in range(len(L)):
                    for j in range(len(L[0])):
                            L[i][j] = Type[idx]
                            idx += 1
                return L
        if function  ==  'I':
            if not isinstance(inputs,tuple) :
                raise ValueError('must be a tuple')
            if inputs[0]<0 or inputs[1]<0:
                raise ValueError('dimensions must be positive')
            matrix  = [ [0 for _ in  range(inputs[1])] for _ in  range(inputs[0])]
            for i in range(inputs[0]):
                for j  in range(inputs[1]):
                    if i ==j:
                        matrix[i][j]=1
            return matrix

        return  inputs #returns initialized list


    @staticmethod
    def matrix_1d(t_L:Union[List,int],function=None,Type=None,):
        #for ones and  zeros
        if isinstance(t_L,List):
            return t_L
        if isinstance(t_L,int) :
            if function is None:
                L =  [Type for _ in range(t_L)]
                return L
            else:
                raise ValueError('must not be a  scalar(list form is a must)')


    @staticmethod
    def zeros(n1=None,n2=None):
        #takes input  as two integers
        if n1 is None: #none case
            raise ValueError('at least 1 dimensions must be provided')
        if n2 is None:# 1D case
            zeros = MatrixCreation.matrix_1d(n1,Type=1)
        else:
            zeros =  MatrixCreation.matrix_2d((n1,n2),Type=1) # 2d case
        return  zeros

    @staticmethod
    def ones(n1=None,n2=None):
        #takes input  as two integers
        if n1 is None: #none case
            raise ValueError('at least 1 dimensions must be provided')
        if n2 is None:# 1D case
            ones = MatrixCreation.matrix_1d(n1,Type=1)# 1 for ones
        else:
            ones =  MatrixCreation.matrix_2d((n1,n2),Type=1) # 2d case
        return  ones

    @staticmethod
    def Identity(x,y):
        if x<0 or y<0:
            raise ValueError('dimensions must be positive')
        I = MatrixCreation.matrix_2d((x,y),function='I',Type=None)
        return I



    @staticmethod
    def normal(low,high,size:Tuple):
        assert low < high ,f'lower bound greater than high,  fix ({low,high})'
        normal = []
        if len(size) == 1:
            normal = [random.uniform(low,high) for i in range(size[0])]
        else:
            normal = MatrixCreation.matrix_2d(size,function='normal',Type=[random.uniform(low,high) for _ in range(size[0]*size[1])])
        return  normal


    @staticmethod
    def randint(x,y):
        if x > y:
            raise ValueError('lower bound must be lesser than  upper bound')
        return random.randint(x,y)

#just for checking  whiles coding,wrote  tests  later
m = MatrixCreation.matrix_2d(2)
print(m)
