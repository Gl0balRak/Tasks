class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        result = -1

        indexes = [0 for _ in edges]
        for current_node in range(len(edges)):
            # Нет смысла проверять ноду которая или не куда не ведет или уже была проверена
            if edges[current_node] < 0:
                continue

            # Считаем длинну цикла
            length = 0
            node = current_node
            while edges[node] >= 0:
                print(node)
                indexes[node] = length
                last_node = node
                node = edges[node]
                edges[last_node] = -(current_node + 2)

                length += 1

            # Если получислся цикл то обновляем ответ
            if edges[node] == -(current_node + 2):
                result = max(result, length - indexes[node])

        return result