# Input: s = "anagram", t = "nagaram"

# Output: true


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            for char in s:
                if s.count(char) != t.count(char):
                    return False
            return True
        return False


sol = Solution()
print(sol.isAnagram("car", t="rat"))
