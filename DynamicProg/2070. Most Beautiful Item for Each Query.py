def binary(arr, n):
    a, b = 0, len(arr)

    while b - a > 1:
        c = (a + b) // 2
        if arr[c][0] > n:
            b = c
        else:
            a = c

    return a


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items += [[-1, 0]]
        items.sort()
        mx = 0
        for i in range(len(items)):
            mx = max(items[i][1], mx)
            items[i][1] = mx
        return [items[binary(items, query)][1] for query in queries]
