from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        checker = strs[0]
        checker_len = len(checker)
        for word in strs[1:]:
            while checker != word[0:checker_len]:
                checker_len -= 1
                if checker_len == 0:
                    return ""
                checker = checker[0:checker_len]
        return checker


sol = Solution()
print(sol.longestCommonPrefix(strs=["fliwer", "flight", "flite"]))
