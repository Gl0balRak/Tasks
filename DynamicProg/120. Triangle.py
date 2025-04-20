class Solution(object):
    def minimumTotal(self, triangle):
        for i in range(1, len(triangle)):
            l = len(triangle[i])-1
            for j in range(l+1):
                if j == 0: triangle[i][0] += triangle[i-1][0]
                elif j == l: triangle[i][l] += triangle[i - 1][-1]
                else: triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])

        return min(triangle[-1])

print(Solution.minimumTotal(None, [[2],[3,4],[6,5,7],[4,1,8,3]]))