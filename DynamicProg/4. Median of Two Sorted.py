# from random import randint
#
#
# def binary(value, array):
#     a, b = 0, len(array) - 1
#     while b - a > 1:
#         c = a + (b - a) // 2
#         if array[c] < value:
#             a = c
#         else:
#             b = c
#     return b
#
# def easy_solution(a, b):
#     result = []
#     while a and b:
#         if a[0] < b[0]:
#             result.append(a.pop(0))
#         else:
#             result.append(b.pop(0))
#     result += a
#     result += b
#     if len(result)%2 == 1:
#         return result[len(result)//2]
#     return (result[len(result)//2] + result[len(result)//2 - 1])/2


def median(arr):
    if len(arr)%2:
        return arr[len(arr)//2]
    return float(arr[len(arr)//2] + arr[len(arr)//2-1])/2

def get_median(arr1, arr2):
    print(arr1, arr2)
    if len(arr1) == 1 or len(arr2) == 1:

        if len(arr2) == 1:
            arr2, arr1 = arr1, arr2
        d = arr1[0]
        a, b = arr2[len(arr2) // 2 - 1], arr2[len(arr2) // 2]

        if (len(arr1) + len(arr2)) % 2:
            if a < d < b: return d
            return a if d < a else b

        c = arr2[len(arr2) // 2 + 1]
        if d < a:
            return float(a + b) / 2
        if d > c:
            return float(c + b) / 2
        return float(d + b) / 2

    if len(arr1) == 2 and len(arr2) == 2:
        arr = list(sorted(arr1 + arr2))
        return float(arr[1] + arr[2]) / 2

    if len(arr2) == 2 or len(arr1) == 2:
        if len(arr2) == 2:
            arr2, arr1 = arr1, arr2

        while len(arr2) > 6:
            arr2 = arr2[1:-1]

        return median(list(sorted(arr1 + arr2)))

    m1 = len(arr1) // 2
    m2 = len(arr2) // 2
    a = arr1[m1]
    b = arr2[m2]
    m = max(min(m1, m2), 2) - 1

    if b > a:
        return get_median(arr2[:-m], arr1[m:])
    return get_median(arr1[:-m], arr2[m:])

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n, m = len(nums1), len(nums2)

        if n == 0:
            return median(nums2)
        if m == 0:
            return median(nums1)

        if n == 1 and m == 1:
            return float(nums1[0]+nums2[0])/2

        return get_median(nums1, nums2)



print(Solution.findMedianSortedArrays(None, [3, 4], [1, 2, 5, 6]))


# TESTS

# tests = [[[1, 2, 3], [4, 6, 7, 9, 12, 13, 15]],
#          [[3, 4, 5, 6, 7], [8, 9, 10, 12, 13, 14, 15, 16, 17]],
#          [[-3, -2, -1, 1, 2, 4, 7, 8], [3, 5, 6, 9, 10, 11, 12, 13]],
#          [[3, 10], [2, 5, 11]],
#          [[1, 2], [3, 4]],
#          [[1, 3], [2]]]
# TEST_LEN = 20
#
#
# for i in range(TEST_LEN-len(tests)):
#     tests.append([[], []])
#     a, b = randint(2, 6), randint(3, 9)
#     while len(tests[-1][1]) != a+b:
#         c = randint(1, a+b+5)
#         if c not in tests[-1][1]:
#             tests[-1][1].append(c)
#
#     tests[-1][0] = list(sorted(list(tests[-1][1])[:a]))
#     tests[-1][1] = list(sorted(list(tests[-1][1])[a:]))
#
#
# for i in range(TEST_LEN):
#     test_data = [tests[i][0].copy(), tests[i][1].copy()]
#     sol1 = Solution.findMedianSortedArrays(None, test_data[0].copy(), test_data[1].copy())
#     test_data2 = [tests[i][0].copy(), tests[i][1].copy()]
#     sol2 = easy_solution(*test_data2)
#
#     if sol1 != sol2:
#         print(f"---- Test {i} ----\nAnswer: {sol1}\nExpected: {sol2}\n{tests[i]}")
#     else:
#         print(f"---- Test {i} ----\nAnswer: {sol1}\nExpected: {sol2}\n")
#

