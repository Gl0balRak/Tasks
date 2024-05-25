import numpy as np

ans = np.array([[12, -5, 5],
               [17, -8, 5],
               [25, -13, 7]])

print(np.linalg.det(np.linalg.matrix_power(ans, -1)))

test = np.array([[-1, -3, -2],
       [0,  2,  2],
       [2,  0, -2]])
result = test.copy()
result = result.dot(test)
result = result.dot(test.T)

print(abs(result))
print(result - abs(ans))
print("dich", sum(sum(abs(result - abs(ans)))))

dif = abs(result) - abs(ans)
differ = abs(sum(sum(dif)))
print(differ)
print(result)