# Problem: Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        print(meetings)
        min_heap = []
        empty = list(range(n))
        count = [0] * n
        for i in range(len(meetings)):
            start, end = meetings[i]
            while min_heap and min_heap[0][0] <= start:
                top = heappop(min_heap)
                heappush(empty, top[1])
            if not empty:
                top = heappop(min_heap)
                heappush(min_heap, (end + top[0] - start, top[1]))
                count[top[1]] += 1
            else:
                room = heappop(empty)
                heappush(min_heap, (end, room))
                count[room] += 1

        return count.index(max(count))
        