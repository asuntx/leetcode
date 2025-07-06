class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for i, char in enumerate(s):
            if char in seen:
                seen[char] = -1
            else:
                seen[char] = i
        for v in seen.values():
            if v != -1:
                return v
        return v


sol = Solution()
print(sol.firstUniqChar(s="loveleetcode"))
