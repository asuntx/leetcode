from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


sol = Solution()
print(sol.removeElement([3, 2, 2, 3, 4, 5, 3], val=3))
