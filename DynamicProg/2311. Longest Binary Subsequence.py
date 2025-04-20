def compare(a, b):
    if len(a) > len(b):
        return False
    if len(a) < len(b):
        return True

    for i in range(len(a)):
        if a[i] < b[i]:
            return True
        elif a[i] > b[i]:
            return False
    return True


class Solution(object):
    def longestSubsequence(self, s, k):
        b = bin(k)[2:]
        bl = len(b)

        for i in range(len(s)):
            subs = s[max(0, len(s)-i-bl):len(s)-i]

            if compare(subs, b):
                count = 0
                for j in range(0, len(s)-i-bl):
                    count += s[j] == '0'
                return count + len(subs)

print(Solution.longestSubsequence(None, "100100001110101", 28946224))
