def invert(f):
    def wrapper(*arg, **kwargs):
        result = f()
        map(abs, result)
    return wrapper

@invert
def foo(number):
    if number >= 0:
        return list(range(0, number, 2))
    return list(range(-((-number-1)//2)*2, 1, 2))



def tests():
    assert foo(6) == [0, -2, -4]
    assert foo(0) == []
    assert foo(-6) == [4, 2, 0]

tests()