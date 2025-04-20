from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits_count = Counter(answers)

        s = 0
        for k, n in rabbits_count.items():
            s += ((n - 1) // (k + 1) + 1) * (k + 1)
        return s