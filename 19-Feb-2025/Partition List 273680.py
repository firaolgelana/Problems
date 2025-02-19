# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_partition = ListNode(0)
        greater_partition = ListNode(0)
        less, greater = less_partition, greater_partition

        while head:
            if head.val < x:
                less_partition.next = head
                less_partition = less_partition.next
            else:
                greater_partition.next = head
                greater_partition = greater_partition.next
                
            head = head.next

        greater_partition.next = None
        less_partition.next = greater.next

        return less.next