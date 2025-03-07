# Problem: Reduce Array Size to Half - https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count, n = Counter(arr), len(arr)
        arr.sort(key=lambda x:(-count[x], x))
        min_removal = len(set(arr[:n//2]))

        return min_removal
