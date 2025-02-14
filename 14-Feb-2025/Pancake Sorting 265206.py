# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        size = len(arr)
        ans = []
        for i in range(size):
            max_num = max(arr[:size - i])
            idx = arr.index(max_num)
            if idx == size - i - 1:
                continue
            if idx == 0:
                arr = arr[:size-i][::-1] + arr[size-i:]
                ans.append(size - i)
            else:
                arr = arr[:idx+1][::-1] + arr[idx+1:]
                ans.append(idx+1)
                arr = arr[:size-i][::-1] + arr[size-i:]
                ans.append(size - i)

        return ans


        