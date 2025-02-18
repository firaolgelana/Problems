# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = Counter(word)
        set_word = set(word)
        for char in set_word:
            count[char] -= 1
            if count[char] == 0:
                del count[char]
            if len(set(count.values())) == 1:
                return True
            count[char] += 1

        return False