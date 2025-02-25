# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class Node:
    def __init__(self, val=""):
        self.val = val
        self.next = None
        self.prev = None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node()
        self.tail = Node()
        self.current = Node(homepage)
        self.head.next = self.current
        self.tail.prev = self.current
        self.current.next = self.tail
        self.current.prev = self.head

    def visit(self, url: str) -> None:
        node = Node(url)
        prev_node, next_node = self.current, self.tail
        prev_node.next = node
        next_node.prev = node
        node.next = next_node
        node.prev = prev_node
        self.current = node

    def back(self, steps: int) -> str:
        while steps and self.current.prev.prev:
            steps -= 1
            self.current = self.current.prev

        return self.current.val

    def forward(self, steps: int) -> str:
        while steps and self.current.next.next:
            steps -= 1
            self.current = self.current.next

        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)