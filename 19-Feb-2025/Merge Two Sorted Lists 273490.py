# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        head = dummy
        while list1 and list2:
            val1, val2 = list1.val, list2.val
            if val1 < val2:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
            
        while list1:
            head.next = list1
            list1 = list1.next
            head = head.next
        
        while list2:
            head.next = list2
            list2 = list2.next
            head = head.next

        return dummy.next
        