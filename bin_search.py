from random import randint, random


def binary(array, n):
    a, b = 0, len(array)-1

    while a <= b:
        mid = (a+b) // 2

        if array[mid] == n:
            return mid
        if array[mid] < n:
            a = mid+1
        else:
            b = mid-1

    return a


for i in range(20):
    array = [randint(1, 1000) for i in range(randint(30, 150))]
    array.sort()

    answer = randint(0, len(array)-1)
    element = array[answer]

    index = binary(array, element)
    if index == answer:
        print("Correct", index, answer)
    else:
        print("Error", index, answer)


def choice(probs):
    _probs_sums = [probs[0]]
    for i in range(1, len(probs)):
        _probs_sums.append(probs[i]+_probs_sums[-1])

    number = random()
    index = binary(_probs_sums, number)

    return index


def sample(size, probs):
    return [choice(probs) for i in range(size)]

print(sample(10, [0.1, 0.4, 0.2, 0.3]))