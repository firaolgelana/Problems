# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(inqueue, process, idx) for idx, (inqueue, process) in enumerate(tasks)]
        tasks.sort()
        heap, ans = [], []
        time = i = 0
        while i < len(tasks) or heap:
            while i < len(tasks) and tasks[i][0] <= time:
                inqueue, process, idx = tasks[i]
                heappush(heap, (process, idx, inqueue))
                i += 1
            
            if i < len(tasks) and tasks[i][0] > time and not heap:
                time = tasks[i][0]
                continue
            process, idx, inqueue = heappop(heap)
            time += process
            ans.append(idx)
            
        return ans