class Solution(object):
    def countPaths(self, grid):
        mn = min(map(min, grid))
        coords = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == mn: coords.append([i, j])


        ways = [1 for i in range(len(grid)) for j in range(len(grid[i]))]


        while coords:
            pass

        """
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] in coords.keys():
                    coords[grid[i][j]].append([i, j])
                else:
                    coords.update({grid[i][j]: [[i, j]]})
        """



print(Solution.countPaths(None, [[1, 1], [3, 4]]))