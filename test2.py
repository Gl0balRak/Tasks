from random import shuffle
from time import perf_counter


def timeit(f):
    def wrapper(*args, **kwargs):
        timer = perf_counter()
        result = f(*args, **kwargs)
        time = perf_counter() - timer
        print(f'[+] {f.__name__} executed in {time}')
        return result
    return wrapper


@timeit
def f1(array: list[str]) -> list[int]:
    return [int(a) for a in array]


@timeit
def f2(array: list[str]) -> list[int]:
    _array = []
    for a in array:
        _array.append(int(a))
    return _array


@timeit
def f3(array: list[str]) -> list[int]:
    return list(map(int, array))


@timeit
def f4(array: list[str]) -> list[int]:
    for i in range(len(array)):
        array[i] = int(array[i])
    return array


@timeit
def y1(array: list[str]) -> list[int]:
    return list(map(str.upper, array))

@timeit
def y2(array: list[str]) -> list[int]:
    return list(map(lambda x: x.upper(), array))


@timeit
def y3(array: list[str]) -> list[int]:
    new = array.copy()
    for i, val in enumerate(new):
        new[i] = val.upper()
    return new


@timeit
def y4(array: list[str]) -> list[int]:
    return [a.upper() for a in array]


@timeit
def y5(array: list[str]) -> list[int]:
    for i, val in enumerate(array):
        array[i] = val.upper()
    return array


data = [str(i) for i in range(4000000)]
shuffle(data)

y1(data.copy())
y2(data.copy())
y3(data.copy())
y4(data.copy())
y5(data.copy())
