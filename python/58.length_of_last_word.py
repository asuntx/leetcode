class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s = s.split(" ")
        return len(s[-1])


sol = Solution()
print(sol.lengthOfLastWord("luffy is still joyboy"))
