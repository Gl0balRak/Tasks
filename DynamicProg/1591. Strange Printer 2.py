class Solution(object):
    def isPrintable(self, targetGrid):
        matrix = targetGrid
        m, n = len(targetGrid), len(targetGrid[0])

        # print(*(list(map(lambda x: list(map(lambda y: y-1, x)), matrix))), sep="\n")
        # print()

        class Color:
            def __init__(self, id):
                self.id = id
                self.rect = [100, 100, 0, 0]
                self.layers = [0 for _ in range(60)]

            def get_point(self, x, y):
                self.rect = [min(self.rect[0], x), min(self.rect[1], y), max(self.rect[2], x), max(self.rect[3], y)]

            def __lt__(self, other):
                return not self.layers[other.id] and not self.__eq__(other)

            def __gt__(self, other):
                return self.layers[other.id] and not self.__eq__(other)

            def __eq__(self, other):
                return self.layers[other.id] == 0 and other.layers[self.id] == 0

            def __le__(self, other):
                return self.__lt__(other) or self.__eq__(other)

            def __ge__(self, other):
                return self.__gt__(other) or self.__eq__(other)

            def __ne__(self, other):
                return not (self.layers[other.id] == 0 and other.layers[self.id] == 0)

        colors = {i: Color(i) for i in range(60)}

        mc = 0

        for x in range(n):
            for y in range(m):
                col = matrix[y][x]-1
                colors[col].get_point(x, y)
                mc = max(mc, col)

        for x in range(n):
            for y in range(m):
                col = matrix[y][x] - 1
                for i in range(mc + 1):
                    rect = colors[i].rect
                    if rect[0] <= x <= rect[2] and rect[1] <= y <= rect[3]:
                        colors[col].layers[i] = 1
        ids = [i for i in range(mc+1) if any(colors[i].layers)]

        cols = [colors[i] for i in range(mc+1) if i in ids]
        cols.sort()

        # print("  " + " ".join(map(lambda x: str(x.id), cols)))
        # for i in range(len(cols)):
        #     d = f"{cols[i].id} "
        #     for j in range(len(cols)):
        #         d += str(cols[i] > cols[j]) + " "
        #     print(d)

        # print(list(map(lambda x: x.id, cols)))
        for i in range(len(cols)):
            for j in range(len(cols)):
                if i != j and ((i < j and cols[i] > cols[j]) or (j < i and cols[j] > cols[i])):
                    # print(cols[i].id, cols[j].id, i, j)
                    return False
        return True


print(Solution.isPrintable(None, [[6,2,2,5],[2,2,2,5],[2,2,2,5],[4,3,3,4]]))