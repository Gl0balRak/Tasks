class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        m, n = [len(matrix), len(matrix[0])]

        def check_square(x, y, ms):
            """
            try:
                for i in range(x, x+ms):
                    try:
                        a = matrix[y][i]
                    except IndexError: return min(x + ms, n), y

                    for j in range(y, y+ms):
                        if matrix[j][i] == "0": return i, j
                return False
            except IndexError: return x, y
            """
            if n-x < ms or m-y < ms:
                return -1, -1

        # def step(x, y, ms, lp):
        #     pos = check_square(x, y, ms)
        #     if pos:
        #         return step(x, y, ms - 1, pos)
        #     return ms, lp
        def step(x, y):
            a, b = 0, min(n, m)
            pos = (x, y)
            lp = pos
            while b - a != 1:
                ms = a + (b - a) // 2
                pos = check_square(x, y, ms)
                if pos:
                    b = ms
                else:
                    a = ms
                if pos: lp = pos
            return a, lp

        result = 0
        x_cut = 0
        # print(*matrix, sep="\n")
        # print()
        while 1:
            one_more = False
            for x in range(x_cut, n):
                if one_more or n-x<result: break
                y = 0
                while y < m:
                    r, pos = step(x, y)
                    if r > result:
                        result = r
                        one_more = True
                    if pos == (-1, -1):

                        break
                    matrix[y][x] = "0"
                    for i in range(x, pos[0]):
                        matrix[pos[1]][i] = "0"

                    y += 1
                x_cut += 1

            if not one_more: break
            if result == min(n, m): break

        return result**2


print(Solution.maximalSquare(None, [["0","0","0","0","1","1","1","0","1"],["0","0","1","1","1","1","1","0","1"],["0","0","0","1","1","1","1","1","0"]]))