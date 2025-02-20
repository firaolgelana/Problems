# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class MyLinkedList:
    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left          
    def get(self, index: int) -> int:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0 and curr != self.right:
            return curr.value
        else:return -1    
    def addAtHead(self, val: int) -> None:
        node, next, prev = Node(val), self.left.next, self.left
        next.prev = node
        prev.next = node
        node.prev = prev
        node.next = next
    def addAtTail(self, val: int) -> None:
        node, next, prev = Node(val), self.right, self.right.prev
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next      
    
    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            node, next, prev = Node(val), curr, curr.prev
            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev
              
    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.right and index == 0:
            next, prev = curr.next, curr.prev
            prev.next = next
            next.prev = prev

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)