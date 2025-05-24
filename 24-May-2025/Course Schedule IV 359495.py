# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for u, v in prerequisites:
            graph[u].append(v)
            in_degree[v] += 1
        
        ancestors = [set() for i in range(numCourses)]
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if ancestors[node]:
                    ancestors[neighbor].update(ancestors[node])
                ancestors[neighbor].add(node)
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        ans = [a in ancestors[b] for a, b in queries]
        return ans
               