# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        lst = ListNode()
        newlst_head = lst
        while head:
            if head.val != val:
                lst.next = head
                lst = lst.next
                head = head.next
                prev = head
            else:
                head = head.next
                lst.next = head
            
        return newlst_head.next