# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        
    def addNum(self, num: int) -> None:
        if len(self.min_heap) == len(self.max_heap):
            if not self.min_heap:
                heappush(self.max_heap, -num)
            else:
                if num > self.min_heap[0]:
                    top = heappop(self.min_heap)
                    heappush(self.max_heap, -top)
                    heappush(self.min_heap, num)
                else:
                    heappush(self.max_heap, -num)
        else:
            if -self.max_heap[0] > num:
                top = -heappop(self.max_heap)
                heappush(self.min_heap, top)
                heappush(self.max_heap, -num)
            else:
                heappush(self.min_heap, num)
                
    def findMedian(self) -> float:
        if len(self.max_heap) + len(self.min_heap) & 1:
            return -self.max_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()