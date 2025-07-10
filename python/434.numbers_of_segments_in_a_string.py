class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split(" "))


sol = Solution()
print(sol.countSegments("Hello, word tomate is  big"))
