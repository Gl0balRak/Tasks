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

data = [str(i) for i in range(4000000)]
shuffle(data)


_data = data.copy()
f1(_data)
print("----------------")

_data = data.copy()
f2(_data)
print("----------------")

_data = data.copy()
f3(_data)
print("----------------")

_data = data.copy()
f4(_data)