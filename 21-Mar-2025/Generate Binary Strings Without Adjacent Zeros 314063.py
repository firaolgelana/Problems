# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        def backtrack(idx, arr):
            if idx == n:
                ans.append("".join(arr[:]))
                return
                            
            for char in '01':
                if arr and arr[-1] == '0' and char == '0':
                    continue
                arr.append(char)
                backtrack(idx + 1, arr)
                arr.pop()
            
        backtrack(0, [])
        return ans

            

        