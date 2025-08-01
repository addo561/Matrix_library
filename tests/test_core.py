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
@pytest.mark.parametrize('test_input,expected',[([[2,2]],[[2,2]]), ([2,2],ValueError) ])
def test_eval(test_input, expected):
    assert matrix_2d(test_input) == expected
