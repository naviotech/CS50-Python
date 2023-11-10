from seasons import validator
from datetime import date
import pytest

def test_validator():
    assert validator('1985-07-24') == date(1985, 7, 24)
    assert validator('1997-07-1') == date(1997, 7, 1)

    with pytest.raises(SystemExit):
        validator('1985-31-01')
    with pytest.raises(SystemExit):
        validator('January 10, 1997')
    with pytest.raises(SystemExit):
        validator('1985/10/10')

   
    