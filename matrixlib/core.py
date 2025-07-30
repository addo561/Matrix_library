# Matrix class and basic operations
# focuses on 1d,2d
from typing_extensions import List,Tuple
from typing import Union
import  random


class MatrixCreation:
    @staticmethod
    def matrix_2d(inputs: Union[List,Tuple],function=None,Type=None):
        if isinstance(inputs,tuple ) and function is None: #for zeros  and ones
            L =  [ [Type for _ in  range(inputs[1])] for _ in  range(inputs[0])]
            return  L

        if  function =='normal':
            L =  [ [0 for _ in  range(inputs[1])] for _ in  range(inputs[0])]
            if Type:
                idx =  0
                for i in range(len(L)):
                    for j in range(len(L[0])):
                            L[i][j] = Type[idx]
                            idx += 1
                return L
        if function  ==  'I':
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
        if isinstance(t_L,int) and function is None:
            L =  [Type for _ in range(t_L)]
            return L
        return t_L #returns initialized list

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
    def Identity(x,y):
        I = []
        I = MatrixCreation.matrix_2d((x,y),function='I',Type=None)
        return I



    @staticmethod
    def normal(low,high,size:Tuple):
        normal = []
        if len(size) == 1:
            normal = [random.uniform(low,high) for i in range(size[0])]
        else:
            normal = MatrixCreation.matrix_2d(size,function='normal',Type=[random.uniform(low,high) for _ in range(size[0]*size[1])])
        return  normal


    @staticmethod
    def randint(x,y):
        return random.randint(x,y)

#just for checking  whiles coding,wrote  tests  later
m = MatrixCreation.Identity(2,2)
print(m)
