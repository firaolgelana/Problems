# Problem: Palindrome Number - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y, copyX = 0, x
        while x > 0:
            y = y * 10 + x % 10
            x //= 10
        return y == copyX


        

        