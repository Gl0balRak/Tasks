from functools import lru_cache


@lru_cache
def get_square(n):
    if n < 4:
        return n
    sqt = int(n**0.5)
    m = 100
    for i in range(1, sqt+1):
        m = min(m, get_square(n-i**2))
    return m + 1


class Solution(object):
    def numSquares(self, n):
        return get_square(n)

print(Solution.numSquares(None, 12))