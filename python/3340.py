class Solution:
    def isBalanced(self, num: str) -> bool:
        even: int = 0
        odd: int = 0
        for i, number in enumerate(num):
            if i % 2 == 0:
                even += int(number)
            else:
                odd += int(number)
        return True if even == odd else False


sol = Solution()
print(sol.isBalanced("24123"))
