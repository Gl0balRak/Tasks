import numpy as np


ans = np.array([[12, -5, 5],
               [17, -8, 5],
               [25, -13, 7]])

mins = [1000000, 0]

for a in range(-3, 3):
    for b in range(-3, 3):
        print("is done")
        for c in range(-3, 3):
            for d in range(-3, 3):
                for e in range(-3, 3):
                    for f in range(-3, 3):
                        for g in range(-3, 3):
                            for h in range(-3, 3):
                                for l in range(-3, 3):
                                    m = np.array([[a, b, c],
                                                  [d, e, f],
                                                  [g, h, l]])
                                    result = m.copy()
                                    result = result.dot(m)
                                    result = result.dot(m)
                                    result = result.dot(m.T)
                                    dif = abs(result) - abs(ans)
                                    differ = abs(sum(sum(abs(dif))))
                                    if differ < mins[0]:
                                        mins = [differ, m]
print(mins)