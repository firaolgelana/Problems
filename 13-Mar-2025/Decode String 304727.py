# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        def decode(idx):
            res = ""
            n = 0
            while idx < len(s):
                if s[idx].isdigit():
                    n = n * 10 + int(s[idx])
                elif s[idx] == '[':
                    new_str, idx = decode(idx + 1)
                    res += new_str * n
                    n = 0
                elif s[idx] == ']':
                    return res, idx
                else:
                    res += s[idx]

                idx += 1
            
            return res, idx

        return decode(0)[0]
            