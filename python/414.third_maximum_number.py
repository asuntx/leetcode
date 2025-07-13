from collections import Counter
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        l = list(nums_counter)
        if len(l) < 3:
            return max(nums)
        l.sort(reverse=True)
        return l[2]


sol = Solution()
print(sol.thirdMax([1, 1, 2]))
