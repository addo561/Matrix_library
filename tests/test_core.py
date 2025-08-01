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

#simple testing ()
@pytest.mark.parametrize(
    'test_input,expected,raises',
    [
        ([[2,2]],[[2,2]],False),
        ([2,2],None,True)
    ]
)
def test_eval(test_input, expected,raises):
    if raises:
        with pytest.raises(ValueError,match='Expected 2D'):
            matrix_2d(test_input)
    else:
        assert matrix_2d(test_input) == expected
