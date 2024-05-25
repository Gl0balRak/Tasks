w = input()


def p(text):
    s = list(text)
    d = {}
    for each in s:
        try:
            d.update({each: 1+d[each]})
        except KeyError:
            d.update({each: 1})

    result = []

    def f(word, symbols):
        if symbols == {}:
            result.append(word)
        for each in symbols.keys():
            s = symbols.copy()
            s[each] -= 1
            if s[each] == 0:
                s.pop(each)
            f(word+each, s)
        return None

    f("", d)

    return result, len(result)

print(p(w))
