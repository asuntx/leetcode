from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return ",".join(Counter(t) - Counter(s))


sol = Solution()
print(sol.findTheDifference("abc", "abcd"))
