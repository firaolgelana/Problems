# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        
        leaf = [u for u in range(numCourses) if indegree[u] == 0]
        queue = deque(leaf)
        ans = []
        while queue:
            current = queue.popleft()
            ans.append(current)
            for neighbor in graph[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return ans if len(ans) == numCourses else []

