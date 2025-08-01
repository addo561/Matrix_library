# Tests for core matrix operations
import pytest
from matrixlib import core

#functions  test
matrix_2d = core.MatrixCreation.matrix_2d
matrix_1d = core.MatrixCreation.matrix_1d
zeros = core.MatrixCreation.zeros
ones = core.MatrixCreation.ones
randint =  core.MatrixCreation.randint
normal =  core.MatrixCreation.normal

#simple testing
# for matrix_2d
@pytest.mark.parametrize(
    'test_input,expected,raises',
    [
        ([[2,2]],[[2,2]],False),
        ([2,2],None,True)
    ]
)
def M2d(test_input, expected,raises):
    if raises:
        with pytest.raises(ValueError,match='Expected 2D'):
            matrix_2d(test_input)
    else:
        assert matrix_2d(test_input) == expected

#for 1D
@pytest.mark.parametrize(
    'test_input,expected,raises',
    [
        ([2,2],[2,2],False),
        ([[2,2]],None,True),
        (2,2,[2,2],False)
    ]
)
def M1d(test_input, expected,raises):
    if raises:
        with pytest.raises(ValueError,match='Expected 2D'):
            matrix_2d(test_input)
    else:
        assert matrix_2d(test_input) == expected
