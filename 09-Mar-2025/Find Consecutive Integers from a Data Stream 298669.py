# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.maps = defaultdict(int)   
        self.k = k
        self.value = value  

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.maps[num] += 1
        else:
            self.maps[self.value] = 0

        return self.maps[self.value] >= self.k
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)