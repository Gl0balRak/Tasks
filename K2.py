def f(n, cars):
    results = []
    maxs = 0
    mins = 0
    maxers = []
    miners = []


    for i in range(n):
        elem = cars[i]

        # Определение mins

        if elem < cars[mins]:
            if i - maxs > 1:
                mins = i

        # Обработка максерсов с текущим значением

        for each in maxers:
            if i - each[1] > 1:
                if each[0] - elem > cars[maxs] - cars[mins]:
                    maxs = each[1]
                    mins = i
                break

        # Дабавление максерсов

        if cars[maxs] < elem:
            maxers.append([elem, i])
            maxers.sort(reverse=True)
            if i - maxers[0][1] > 2:
                maxers = [maxers[0]]
            p = 100000000000
            for i in range(len(maxers)):
                if i - maxers[i][1] > 1:
                    p = i
                    break
            maxers = maxers[:i+1]


        results.append(cars[maxs]-cars[mins])

    return results

"""

12
5 3 2 4 5 6 19 18 17 20 4 29

"""

if __name__ == "__main__":
    n = int(input())
    cars = list(map(int, input().split()))
    print(*f(n, cars))