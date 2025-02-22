# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(left, right):
            curr, prev = left, right
            while curr != right:
                temp = curr
                curr = curr.next
                temp.next = prev
                prev = temp
            return prev

        dummy = ListNode(0, head)
        prev = dummy
        curr = dummy
        while True:
            for i in range(k):
                curr = curr.next
                if not curr:
                    return dummy.next

            new_start = reverse(prev.next, curr.next)
            temp = prev.next
            prev.next = new_start
            prev = temp       
            curr = prev
        