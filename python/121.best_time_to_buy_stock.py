from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in prices:
            if buy > i:
                buy = i
                continue
            if i - buy > profit:
                profit = i - buy
        return profit


sol = Solution()
print(sol.maxProfit([2, 4, 1]))
