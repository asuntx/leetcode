from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i not in nums:
                return i
        return max(nums) + 1


sol = Solution()
print(sol.missingNumber([0]))
