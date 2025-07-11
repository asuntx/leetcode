from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = Counter(nums)
        return n.most_common()[-1][0]


sol = Solution()
print(sol.singleNumber([1]))
