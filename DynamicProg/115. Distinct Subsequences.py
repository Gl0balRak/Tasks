"""
class Solution(object):
    def numDistinct(self, s, t):
        lt = len(t) - 1
        ls = len(s) - 1
        num_s = [0 for i in range(ls + 1)]
        for i in range(lt):
            t1 = t[lt - i]
            t2 = t[lt - i - 1]
            c = 0
            for j in range(ls + 1):
                s1 = s[ls - j]
                if s1 == t1: c += num_s[ls-j]
                if s1 == t2 and j > i: num_s[ls - j] = c
            #print("\n".join(map(str, num_s)))
            #print()
        res = 0
        sym = t[0]
        for j in range(lt, ls + 1):
            if s[ls - j] == sym: res += num_s[ls-j]
        return res
"""
class Solution(object):
    def numDistinct(self, s, t):
        lt = len(t) - 1
        ls = len(s) - 1
        num_s = [int(s[i] == t[-1]) for i in range(ls + 1)]

        for j in range(lt):
            c_sym = t[lt-j]
            n_sym = t[lt-j-1]
            c = 0
            _num_s = [0 for i in range(ls + 1)]
            for i in range(ls+1):
                let = s[ls-i]
                if let == n_sym: _num_s[ls-i] = c
                if let == c_sym: c += num_s[ls-i]
            num_s = _num_s
        return sum(num_s)


print(Solution.numDistinct(None, "babgbag", "bag"))

