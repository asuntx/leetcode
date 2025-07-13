from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        for key, value in nums_counter.items():
            if value >= len(nums) / 2:
                return key


sol = Solution()
print(sol.majorityElement(nums=[1, 1, 1, 2, 2, 2]))
