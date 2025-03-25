# Problem: Maximum Score Words Formed by Letters - https://leetcode.com/problems/maximum-score-words-formed-by-letters/description/

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def check(word, letter_count):
            word_count = Counter(word)
            for char in word_count:
                if word_count[char] > letter_count[char]:
                    return True
            return False
            
        letter_count = Counter(letters)
        self.ans = 0
        def backtrack(idx, count):
            if idx == len(words):
                return 
            for i in range(idx, len(words)):
                word = words[i]
                if check(word, letter_count):
                    continue
                for char in word:
                    count += score[ord(char) - 97]
                    letter_count[char] -= 1
                self.ans = max(self.ans, count)
                backtrack(i + 1, count)
                for char in word:
                    letter_count[char] += 1
                    count -= score[ord(char) - 97]
                    
        backtrack(0, 0)
        return self.ans

                


