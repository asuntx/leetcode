from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sequence = list(s)
        sub = list(t)
        count = 0
        n: List = []
        if len(sequence) == 0:
            return True
        for char in sub:
            if count == len(sequence):
                count = 0
            if char in sequence[count]:
                n.append(char)
                count += 1
        return n == sequence


sol = Solution()
print(sol.isSubsequence("", "bbbbbbbbbbbbbbbbbbahbgdc"))
