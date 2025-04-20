class Solution(object):
    def minimumNumbers(self, num, k):
        if num == 0: return 0

        u = num % 10

        ost = [k]
        while ost[-1] != ost[0] or len(ost) == 1:
            ost.append((ost[-1]+k)%10)
        ost = ost[:-1]
        if not u in ost:
            return -1

        res = ost.index(u) + 1

        if k*res > num: return -1

        return res

print(Solution.minimumNumbers(None, 5, 1))
