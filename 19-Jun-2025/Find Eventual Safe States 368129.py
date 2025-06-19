# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ingoing = [[] for _ in range(len(graph))]
        outdegree = [0] * len(graph)
        for i in range(len(graph)):
            for node in graph[i]:
                ingoing[node].append(i)
                outdegree[i] += 1

        terminal_node = deque([i for i in range(len(graph)) if not graph[i]])
        safe_node = []
        while terminal_node:
            current = terminal_node.popleft()
            safe_node.append(current)
            for neighbor in ingoing[current]:
                outdegree[neighbor] -= 1
                if outdegree[neighbor] == 0:
                    terminal_node.append(neighbor)
        safe_node.sort()

        return safe_node

        