class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        m, n = [len(matrix), len(matrix[0])]
        matrix.append(["0"]*n)
        for i in range(m+1): matrix[i].append("0")

        def check_square(x, y, ms):
            if x+ms > n or y+ms > m: return False

            for i in range(x, x + ms):
                for j in range(y, y + ms):
                    if matrix[j][i] == "0": return False
            return True

        def fill_square(x, y, ms):
            for j in range(y, min(y+ms+1, m+1)):
                for i in range(x, min(x+ms+1, n+1)):
                    if matrix[j][i] == "0":
                        for l in range(x, i+1):
                            matrix[j][l] = "0"
                        break
            matrix[y][x] = "0"

        def get_max_square(x, y):
            a, b = 0, min(n, m)*2
            while b - a != 1:
                ms = a + (b - a) // 2
                if check_square(x, y, ms):
                    a = ms
                else:
                    b = ms
            return a

        result = 0
        # print(*matrix, sep="\n")
        # print()
        x = 0
        while x < n-result:
            for y in range(m):
                if matrix[y][x] == "1":
                    r = get_max_square(x, y)
                    fill_square(x, y, r)
                    # print(r)
                    # print(*matrix, sep="\n")
                    # print()
                    if r>result:
                        result = r
                        x -= 1
                        break
            x += 1
        return result**2


print(Solution.maximalSquare(None, [["1"]]))