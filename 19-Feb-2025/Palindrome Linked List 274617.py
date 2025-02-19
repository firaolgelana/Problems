# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        current_node, prev = slow, None
        while current_node:
            temp = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = temp
        
        while prev and head:
            if prev.val != head.val:
                return False
            head = head.next
            prev = prev.next
            
        return True

        