def func(a,b):
    return a+b

def test_add():
    assert func(1,3) == 4
    assert func(1,-1) == 0