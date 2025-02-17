# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shifts_s = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            if direction:
                shifts_s[start] += 1
                shifts_s[end + 1] -= 1
            else:
                shifts_s[start] -= 1
                shifts_s[end + 1] += 1

        for i in range(len(s)):
            shifts_s[i + 1] += shifts_s[i]

        for i in range(len(s)):
            char = chr((ord(s[i]) - 97 + shifts_s[i]) % 26 + 97)
            shifts_s[i] = char

        return "".join(shifts_s[:-1])      