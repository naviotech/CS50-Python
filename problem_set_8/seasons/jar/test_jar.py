from jar import Jar
import pytest
def test_init():
    cookies = Jar(40,38)
    assert cookies.capacity == 40
    assert cookies.size == 38

    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    cookies = Jar(12)
    cookies.deposit(7)
    assert cookies.size == 7

    cookies= Jar(12,11)
    with pytest.raises(ValueError):
        cookies.deposit(5)


def test_withdraw():
    cookies = Jar(12)
    cookies.deposit(7)
    cookies.withdraw(2)
    assert cookies.size == 5

    cookies = Jar(12,1)
    with pytest.raises(ValueError):
        cookies.withdraw(6)

