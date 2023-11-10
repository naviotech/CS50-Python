from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("2/4") == 50
    assert convert("1/8") == 12
    assert convert("2/3") == 67
    assert convert("0/100") == 0
    assert convert("100/100") == 100
    assert convert("4/8") == 50

    with pytest.raises(ValueError):
        convert("6/4")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("Cat/dog")
    
def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(10) == "10%"
    assert gauge(60) == "60%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
