from math import *


def f(a, b):
    return a**2 + 3*a*b - 54, 4*b*b + a*b - 115


mins = [1111111, 0, 0, 0]


for x in range(1000):
    for y in range(1000):
        c = f(x, y)
        k = abs(c[0] - c[1])
        if k < 5:
            if k < mins[0]:
                mins = [k, c[0], c[1], [x, y]]
            print(str(x) + ", " + str(y) + ":", c[0], "=", c[1])

print("Мин:", mins[0], "x:", mins[3], "1:", mins[1], "2:", mins[2])