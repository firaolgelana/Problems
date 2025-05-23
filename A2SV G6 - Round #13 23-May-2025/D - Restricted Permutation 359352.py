# Problem: D - Restricted Permutation - https://codeforces.com/gym/607625/problem/D

from heapq import heapify, heappop, heappush
n, m = map(int, input().split())
indegree = [0] * n
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    indegree[v] += 1

heap = [i for i in range(n) if indegree[i] == 0]
heapify(heap)
ans = []
while heap:
    current = heappop(heap)
    ans.append(current + 1)
    for neighbor in graph[current]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            heappush(heap, neighbor)

if len(ans) == n:
    print(*ans) 
else:
    print(-1)
    

    