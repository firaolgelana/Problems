# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_string = defaultdict(int)
        max_length = left = 0
        for right in range(len(s)):
            sub_string[s[right]] += 1
            while right - left + 1 > len(sub_string):
                sub_string[s[left]] -= 1
                if sub_string[s[left]] == 0:
                    del sub_string[s[left]]
                left += 1
            max_length = max(max_length, len(sub_string))

        return max_length

 