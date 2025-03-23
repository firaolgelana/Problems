# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def backtrack(idx, arr):
            if idx == len(s):
                if len(arr) == 4:
                    ans.append(".".join(arr))
                return
            if len(arr) == 4:
                return
            
            for i in range(idx, len(s)):
                ip = s[idx:i+1]
                if len(ip) != len(str(int(ip))):
                    continue
                if int(ip) > 255:
                    continue
                arr.append(ip)
                backtrack(i + 1, arr)
                arr.pop()

        backtrack(0, [])
        return ans
        