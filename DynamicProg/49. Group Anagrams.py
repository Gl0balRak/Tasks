class Anagram:
    def __init__(self, string):
        self.string = string
        self.letters = ""
        self._get_letters()

    def _get_letters(self):
        """
        for sym in self.string:
            self.letters[sym] = self.letters.setdefault(sym, 0) + 1
        """
        self.letters = "".join(sorted(self.string))

    def __eq__(self, other):
        return self.letters == other.letters

    def __repr__(self):
        return self.letters.__repr__()

    def __hash__(self):
        return hash(self.letters)


class Solution(object):
    def groupAnagrams(self, array):
        array = list(map(lambda x: ["".join(sorted(x)), x], array))
        array.sort()
        d = []
        result = []
        abc = ""
        while array:
            elem = array.pop(0)
            if d:
                if elem[0] == abc or not abc:
                    d.append(elem[1])
                    continue
                result.append(d)
            d = [elem[1]]
            abc = elem[0]
        result.append(d)

        return result

print(Solution.groupAnagrams(None, ["eat","tea","tan","ate","nat","bat"]))
