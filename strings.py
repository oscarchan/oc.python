'''
   string test
   In python 2,
      string is a serie of bytes
   In python 3,
      string is a serie of char
'''

class TObject(object):
    def __init__(self, value = None):
        self.value = str(value)

    def __str__(self):
        return "TObj(" + self.value + ").s"

    def __repr__(self):
        return "TObj(" + self.value + ").r"

class SObject(object):
    def __init__(self, value = None):
        self.value = str(value)

    def __str__(self):
        return "SObj(" + self.value + ").s"

class RObject(object):
    def __init__(self, value = None):
        self.value = str(value)

    def __repr__(self):
        return "RObj(" + self.value + ").r"

def test_str():
    """
    NOTE: python logging uses str() instead of repr() on object, but repr() on elements of collections
    """
    o1 = TObject(1)
    s2 = SObject(2)
    r3 = RObject(3)

    assert str(o1) == o1.__str__()
    assert str(s2) == s2.__str__()
    assert str(r3) == r3.__repr__()   # str() uses __repr__() if __str__() does not exist

def test_repr():
    o1 = TObject(1)
    s2 = SObject(2)
    r3 = RObject(3)

    assert repr(o1) == o1.__repr__()
    assert repr(s2) != s2.__str__()   # repr() does not use __str__() if __repr() does not exist
    assert repr(r3) == r3.__repr__()


def test_find():
    # string.find(s, sub[, start[, end]])

    assert "a.b.c.d".find(".", 0) == 1
    assert "a.b.c.d".find(".", 1) == 1
    assert "a.b.c.d".find(".", 2) == 3

    assert "a.b.c.d".find("-", 0) == -1

def test_find2():
    first_index = "a.b.c.d".find(".", 0)

    assert "a.b.c.d".find(".", first_index + 1) == 3

def test_length():
    s = "abc"
    assert 3 == len(s)

def test_conditions():
    assert not ""
    assert not None
    assert "random strings"

def test_startswith():
    key = "prefix.key"
    prefix = "prefix."
    assert key.startswith(prefix)
    assert "key" == key[len(prefix):]

