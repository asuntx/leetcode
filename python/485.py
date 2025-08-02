from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        got_length = []
        length:int = 0
        for num in nums:
            if num == 0:
                got_length.append(length)
                length = 0
            else:
                length +=1
        got_length.append(length)
        return max(got_length)
sol = Solution()
print(sol.findMaxConsecutiveOnes(nums=[1,1,0,1,1,1]))
