# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_substring(count1, count2):
            for key in count1:
                if count1[key] > count2[key]:
                    return False
            return True
            
        size = len(s)
        count_t = Counter(t)
        count_s = defaultdict(int)
        left, start, end = 0, 0, size + 1
        for right in range(size):
            count_s[s[right]] += 1
            while is_substring(count_t, count_s):
                count_s[s[left]] -= 1
                if count_s[s[left]] == 0:
                    del count_s[s[left]]
                if right - left < end - start:
                    start, end = left, right
                left += 1

        return s[start:end + 1] if end != size + 1 else ""