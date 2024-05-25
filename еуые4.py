text = "qwerty 121234"


def crop(s: str, n: int) -> str:
    if n >= len(s): return s

    n = max(0, n)
    for i in range(0, n+1):
        if s[n-i] == " ":
            return s[:n-i]
    return ""


def crop(s: str, n: int) -> int:
    _s = s[:n].split()

    while len(_s[-1]) in range(1, 4):
        _s = _s[:-1]
        if not _s: return ""
    return " ".join(_s)


print(crop(text, 11))

