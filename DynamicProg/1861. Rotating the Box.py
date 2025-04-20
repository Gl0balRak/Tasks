class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for layer in box:
            stones = 0
            for j in range(len(layer)):
                if layer[j] == "#":
                    layer[j] = "."
                    stones += 1
                elif layer[j] == "*":
                    for k in range(stones):
                        layer[j - k - 1] = "#"
                    stones = 0
            for k in range(stones):
                layer[len(layer) - k - 1] = "#"

        return [[box[len(box) - 1 - i][j] for i in range(len(box))] for j in range(len(box[0]))]

