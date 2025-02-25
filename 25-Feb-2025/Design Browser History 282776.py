# Problem: Design Browser History - https://leetcode.com/problems/design-browser-history/description/

class Node:
    def __init__(self, val=""):
        self.val = val
        self.next = None
        self.prev = None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(homepage)        

    def visit(self, url: str) -> None:
        node = Node(url)
        self.current.next = node
        node.prev = self.current
        self.current = node

    def back(self, steps: int) -> str:
        while steps and self.current.prev:
            steps -= 1
            self.current = self.current.prev

        return self.current.val

    def forward(self, steps: int) -> str:
        while steps and self.current.next:
            steps -= 1
            self.current = self.current.next

        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)