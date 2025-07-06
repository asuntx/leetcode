from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = len(s) - 1
        j = 0
        while i > j:
            s[i], s[j] = s[j], s[i]
            j += 1
            i -= 1


sol = Solution()
print(sol.reverseString(s=["h", "o", "l", "a"]))
