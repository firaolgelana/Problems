# Problem: Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.appendleft(x)
        
    def pop(self) -> int:
        self.queue.rotate(-1)
        removed = self.queue.pop()
        return removed

    def top(self) -> int:
        self.queue.rotate(-1)
        top = self.queue.pop()
        self.queue.appendleft(top)
        return top

    def empty(self) -> bool:
        return not self.queue
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()