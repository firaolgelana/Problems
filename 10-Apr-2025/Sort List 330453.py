# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(left_node, right_node):
            merged = ListNode()
            tail = merged
            while left_node and right_node:
                val1, val2 = left_node.val, right_node.val
                if val1 <= val2:
                    tail.next = left_node
                    left_node = left_node.next
                else:
                    tail.next = right_node
                    right_node = right_node.next
                tail = tail.next
            tail.next = left_node or right_node

            return merged.next

        if not head or not head.next:
            return head

        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
        return merge(left, right)

        