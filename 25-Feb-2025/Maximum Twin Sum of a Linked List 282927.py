# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        def reverse(node):
            prev = None
            while node:
                current = node
                node = node.next
                current.next = prev
                prev = current

            return prev

        first_half = head
        second_half = reverse(slow)
        max_twin_sum = float('-inf')
        while second_half:
            max_twin_sum = max(max_twin_sum, first_half.val + second_half.val)
            first_half = first_half.next
            second_half = second_half.next  

        return max_twin_sum      

        