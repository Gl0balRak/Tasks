class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        m, n = [len(matrix), len(matrix[0])]
        # if m != len(matrix):
        #     matrix = [[matrix[i][j] for i in range(n)]for j in range(m)]
        # print(m, n)
        def check_square(x, y, ms):
            try:
                for i in range(x, x+ms):
                    for j in range(y, y+ms):
                        if matrix[j][i] == "0": return False
                return True
            except IndexError: return False

        class Worker:
            def __init__(self):
                self.result = 0

            def step(self, x, y, ms):
                if check_square(x, y, ms):
                    self.result = max(self.result, ms)
                    return self.step(x, y, ms+1)
                return
        w = Worker()

        for x in range(0, n):
            for y in range(0, m):
                w.step(x, y, 1)

        return w.result**2


print(Solution.maximalSquare(None, [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))