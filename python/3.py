from typing import Dict, List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring: List[str] = []
        lens: List[int] = []
        for index, char in enumerate(s):
            print(substring, lens)
            if char not in substring:
                substring.append(char)
            else:
                lens.append(len(substring))
                substring.clear()
        return max(lens)


sol = Solution()
print(sol.lengthOfLongestSubstring("pwwkew"))
