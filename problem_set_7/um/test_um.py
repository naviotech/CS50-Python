from um import count

def test_count():
    assert count("um, hello, um, world") == 2
    assert count("um...") == 1
    assert count("yum") == 0
    assert count("yummy") == 0

    assert count("¿um?") == 1
    assert count("um, thanks, um...") == 2
    assert count("um um um um um") == 5
    assert count("UM..") == 1