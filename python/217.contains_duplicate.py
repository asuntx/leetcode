from collections import Counter
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_counter = Counter(nums)
        for value in nums_counter.values():
            if value >= 2:
                return True
        return False


sol = Solution()
print(sol.containsDuplicate([1, 2, 3]))
