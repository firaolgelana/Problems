# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head

        current = head
        node = odd = head.next

        while current and current.next and current.next.next:
            current.next = current.next.next
            current = current.next
            odd.next = current.next
            odd = odd.next
        
        current.next = node
        
        return head