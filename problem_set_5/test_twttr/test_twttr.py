from twttr import shorten

def testing_twttr():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("twitter") == "twttr"
    assert shorten("TWITER") == "TWTR"
    assert shorten("I'm fine!") == "'m fn!"
    assert shorten("1a2be") == "12b"