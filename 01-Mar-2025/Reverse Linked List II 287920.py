# Problem: Reverse Linked List II - https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        for i in range(left - 1):
            prev = prev.next
        
        current_node, rev = prev.next, None
        for i in range(right - left + 1):
            next_node = current_node.next
            current_node.next = rev
            rev = current_node
            current_node = next_node
        
        prev.next.next = current_node
        prev.next = rev

        return dummy.next
        
        