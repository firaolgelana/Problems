# Problem: Smallest Number in Infinite Set - https://leetcode.com/problems/smallest-number-in-infinite-set/description/

class SmallestInfiniteSet:

    def __init__(self):
        self.min_heap = list(range(1, 1001))
        self.maps = Counter(range(1, 1001))

    def popSmallest(self) -> int:
        min_num = heappop(self.min_heap)
        del self.maps[min_num]
        return min_num

    def addBack(self, num: int) -> None:
        if num not in self.maps:
            self.maps[num] = 1
            heappush(self.min_heap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)