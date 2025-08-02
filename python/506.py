from typing import List
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_sorted = score.sort(reverse=True)
        result = []
        for point in score:
            s = score_sorted.index(point)
            if s == 0:
                result.append()
        return score
sol = Solution()
print(sol.findRelativeRanks(score=[1,4,3,2,5]))
