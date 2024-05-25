def f2(n, cars):
    anser = ""
    result, maxers, abs_max = [], [], 0
    for i in range(n):
        elem = cars[i]
        result.append(elem)
        abs_max = max(abs_max, elem)
        maxers.append(abs_max)
        if len(result) <= 2:
            anser += "0 "
        else:
            h = 0
            for j in range(1, len(result) - 1):
                h = max(h, maxers[j - 1] - min(result[j + 1:]))
            anser += str(h) + " "
    return anser.strip()


if __name__ == "__main__":
    n, cars = int(input()), list(map(int, input().split()))
    print(f2(n, cars))
