from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()


sol = Solution()
print(sol.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, n=3, nums2=[2, 5, 6]))
