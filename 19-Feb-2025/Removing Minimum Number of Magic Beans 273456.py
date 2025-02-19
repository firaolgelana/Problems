# Problem: Removing Minimum Number of Magic Beans - https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort(reverse=True)
        max_nonRemoval = float('-inf')
        
        for i in range(len(beans)):
            max_nonRemoval = max(max_nonRemoval, beans[i] * (i + 1))

        return sum(beans) - max_nonRemoval
        