def carry(f):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (tuple(args), tuple(kwargs.items()))

        if key in cache:
            return cache[key]

        result = f(*args, **kwargs)
        cache.update({key: result})

        return result
    return wrapper


@carry
def f(n):
    if n in [1, 2]: return 1
    return f(n-1) + f(n-2)

@carry
def f1(n):
    return n**2


for i in range(1, 50):
    print(i, f(i))