class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        degree = [0 for i in range(n)]

        for edge in edges:
            degree[edge[1]] += 1

        champs = [i for i in range(len(degree)) if not degree[i]]

        if len(champs) == 1:
            return champs[0]
        return -1