from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))


sol = Solution()
print(sol.intersection([4, 9, 5], [9, 4, 9, 8, 4]))
