word = input("")
symbols = []

for each in word:
    symbols.append(each)

kolvo = 0


def filtr(array):
    res = []
    for each in array:
        if not each in res:
            res.append(each)
    return res


dich = []


def f(s, res):
    global kolvo
    if s == []:
        return res
    for each in s:
        a = s.copy()
        a.remove(each)
        result = f(a, res + [each])
        if not result is None:
            kolvo += 1
            dich.append(result)

f(symbols, [])
print(len(dich))

