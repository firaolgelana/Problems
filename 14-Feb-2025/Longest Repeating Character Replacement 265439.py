# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, longest = 0, 0
        window = defaultdict(int)
        for right in range(len(s)):
            window[s[right]] += 1
            if right - left + 1 - max(window.values()) > k:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1

            longest = max(longest, right - left + 1)
        
        return longest


        