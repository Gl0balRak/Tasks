# class Solution(object):
#     def longestCycle(self, edges):
#         edges = [each if each != -1 else len(edges) for each in edges]
#         _edges = [each for each in edges]
#
#         ### next = edges(cur)
#         result = -1
#         for i in range(len(edges)):
#             if _edges[i] > 0:
#                 next = _edges[i]
#                 cur = i
#                 cycle = True
#                 while next != -(i+1):
#                     if next < 0:
#                         cycle = False
#                         break
#                     cur = next
#                     if cur >= len(edges):
#                         cycle = False
#                         break
#                     next = _edges[cur]
#                     _edges[cur] = -(i+1)
#                 if cycle:
#                     l = 1
#                     start = cur
#                     cur = edges[cur]
#                     while cur != start:
#                         cur = edges[cur]
#                         l += 1
#                     result = max(result, l)
#         return result
#
# print(Solution.longestCycle(None, [3,4,0,2,-1,2]))
#
