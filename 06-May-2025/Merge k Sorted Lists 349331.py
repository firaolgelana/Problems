# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for nums in lists:
            head = nums
            while head:
                heappush(heap, head.val)
                head = head.next
        sortedList = ListNode()
        dummy = sortedList
        while heap:
            top = heappop(heap)
            node = ListNode(top)
            dummy.next = node
            dummy = dummy.next
        
        return sortedList.next
        

        