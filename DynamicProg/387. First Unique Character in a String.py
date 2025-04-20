from string import ascii_lowercase


class Solution(object):
    def firstUniqChar(self, s):
        letters = {let: -1 for let in ascii_lowercase}

        for i, sym in enumerate(s):
            if sym in letters:
                a = letters[sym]
                if a == -1:
                    letters[sym] = i
                else:
                    letters.pop(sym)

        indexs = [value for value in letters.values() if value != -1]
        if indexs:
            return min(indexs)
        return -1

print(Solution.firstUniqChar(None, "aabb"))