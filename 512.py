j = 0


def a(x):
    if x == "Y":
        return 1
    return 0


n, m, k = list(map(int, input().split(" ")))


mp = []

for i in range(n):
    label = list(map(a, input()))
    mp.append(label)

while [0]*m in mp:
    mp.remove([0]*m)
    n -= 1


def count(maps):

    for i in range(m):
        maps[0][i] = [maps[0][i]]*m
        maps[0][i][i] = 0

    for y in range(1, n):
        for x in range(m):
            if maps[y][x] == 1:
                result = []
                for j in range(m):
                    if y + 1 < n: s = sum(list(map(lambda t: min(t[j], t[x]), maps[y-1])))
                    else: s = sum(list(map(lambda t: t[j], maps[y-1])))
                    result.append(s)
                result[x] = 0
                maps[y][x] = result
            else:
                maps[y][x] = [0]*m

    answer = sum(list(map(max, maps[n-1])))
    return answer


print(count(mp))










"""

3 4 3
YYYN
NYNY
YYYN


10 10 10
YYYYYYYYYY
YYYYYYYYYY
YYYYYYYYYY
YYYYYYYYYY
YYYYYYYYYY
YYYYYYYYYY
YYYYYYYYYY
YYYYYYYYYY
YYYYYYYYYY
YYYYYYYYYY

"""



"""


def b(x):
    global j
    return x[:j] + x[j+1:]


def c(maps):
    global j

    length = len(maps)

    if length == 0:
        return 1

    result = 0
    for i in range(len(maps[0])):
        if maps[0][i]:
            j = i
            k = maps.copy()
            k = k[1:]
            k = list(map(d, k))
            result += c(k)

    return result
"""