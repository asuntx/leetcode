from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return Counter(ransomNote) - Counter(magazine) == {}


sol = Solution()
print(sol.canConstruct("bac", "ab"))
