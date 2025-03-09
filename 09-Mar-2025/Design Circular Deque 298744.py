# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class LinkedList:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.count = 0
        self.head = LinkedList()
        self.tail = LinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head      

    def insertFront(self, value: int) -> bool:
        if self.count >= self.k:
            return False
        self.count += 1
        node = LinkedList(value)
        prev_node, next_node = self.head, self.head.next
        prev_node.next = node
        next_node.prev = node
        node.prev = prev_node
        node.next = next_node
        return True

    def insertLast(self, value: int) -> bool:
        if self.count >= self.k:
            return False
        self.count += 1
        node = LinkedList(value)
        prev_node, next_node = self.tail.prev, self.tail
        prev_node.next = node
        next_node.prev = node
        node.prev = prev_node
        node.next = next_node
        return True

    def deleteFront(self) -> bool:
        if not self.head.next.next:
            return False
        self.count -= 1
        deleted_node = self.head.next
        self.head.next = deleted_node.next
        deleted_node.next.prev = self.head
        return True

    def deleteLast(self) -> bool:
        if not self.head.next.next:
            return False
        self.count -= 1
        deleted_node = self.tail.prev
        self.tail.prev = deleted_node.prev
        deleted_node.prev.next = self.tail
        return True

    def getFront(self) -> int:
        if not self.head.next.next:
            return -1

        return self.head.next.val

    def getRear(self) -> int:
        if not self.head.next.next:
            return -1
        
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        return not self.head.next.next
        
    def isFull(self) -> bool:
        return self.count >= self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()