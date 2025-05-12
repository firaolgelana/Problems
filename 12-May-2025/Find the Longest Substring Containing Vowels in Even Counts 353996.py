# Problem: Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mask = 0
        ans = 0
        vowels = 'aeiou'
        mask_to_idx = {0:-1}
        for i, char in enumerate(s):
            if char in vowels:
                mask ^= (1 + ord(char) - ord('a'))
            if mask in mask_to_idx:
                ans = max(ans, i - mask_to_idx[mask])
            else:
                mask_to_idx[mask] = i
                
        return ans
        