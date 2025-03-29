# Problem: Time Based Key-Value Store - https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        self.maps = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.maps[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.maps:
            return ""
        lst = self.maps[key]
        left, right = 0, len(lst) - 1
        while left <= right:
            mid = (left + right) // 2
            if lst[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1
        return lst[left - 1][1] if left > 0 else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)