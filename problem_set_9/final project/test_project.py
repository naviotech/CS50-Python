from project import first_handling_errors,second_handling_errors,tee_calculate
import pytest


def test_tee_calculate():
    assert tee_calculate([1700,1]) == 2040

def test_first_handling_errors():
    with pytest.raises(ValueError):
        first_handling_errors("","","2")
    with pytest.raises(TypeError):
        first_handling_errors("hello","4","2")

def test_second_handling_errors():
    with pytest.raises(ValueError):
        second_handling_errors(70,26,174,1,0)