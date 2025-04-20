class Solution(object):
    def findLongestChain(self, pairs):
        pairs.sort()
        nums = [0 for i in range(len(pairs))]


Solution.findLongestChain(None, [[1,2],[2,3],[3,4]])