# Problem: Find K Pairs with Smallest Sums - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap = []
        for i in range(len(nums2)):
            heappush(min_heap, (nums1[0] + nums2[i], 0, i))

        ans = []
        for _ in range(k):
            _sum, i, j = heappop(min_heap)
            if i + 1 < len(nums1):
                heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))
            ans.append([nums1[i], nums2[j]])

        return ans
            


        