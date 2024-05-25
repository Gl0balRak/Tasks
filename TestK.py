from Tasks.K import f2
from Tasks.K2 import f
from random import randint


def create_tasks(n, l=[4, 12], s=[1, 20]):
    result = [[randint(s[0], s[1]) for j in range(randint(l[0], l[1]))] for i in range(n)]
    return result

if __name__ == "__main__":
    r = create_tasks(15)
    for task in r:
        print("Task: ", *task)
        _f = f(len(task), task)
        _f2 = f2(len(task), task)
        print("F: {}".format(_f))
        print("Right answer: {}".format(_f2))
