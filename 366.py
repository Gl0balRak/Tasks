n, s = list(map(int, input().split(" ")))
numbers = list(map(int, input().split(" ")))

o = numbers[n-1]


def a(i, k, l):
    p = sum(numbers[i:])
    if k + p < s:
        return None
    elif k - p > s:
        return None
    elif k + p == s:
        return l + ["+"]*(n-i)
    elif k - p == s:
        return l + ["-"]*(n-i)
    else:
        r1 = a(i+1, numbers[i] + k, l+["+"])
        if r1 is not None:
            return r1

        r2 = a(i+1, k - numbers[i], l+["-"])

        if r2 is not None:
            return r2

        return None


r = a(1, numbers[0], ["+"])
if r is not None:
    result = ""
    result += str(numbers[0])
    for i in range(1, n):
        result += str(r[i])
        result += str(numbers[i])

    print(result+"="+str(s))

else:
    print("No solution")