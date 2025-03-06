# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for folder in logs:
            if folder == './':
                continue
            elif folder == '../':
                if stack:
                    stack.pop()
            else:
                stack.append(folder)

        return len(stack)
        