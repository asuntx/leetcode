from collections import Counter
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits[-1] == 9:
            digits[-1] = digits[-1] + 1
            return digits
        if Counter(digits).get(9) == len(digits):
            l = [1]
            for i in range(0, len(digits)):
                l.append(0)
            return l

        reverse_index = []
        for i in range(len(digits) - 1, -1, -1):
            reverse_index.append(i)

        for i, num in enumerate(digits[::-1]):
            if num != 9:
                i = reverse_index.index(i)
                digits[i] = num + 1
                for i in range(i + 1, len(digits)):
                    digits[i] = 0
                return digits


sol = Solution()
print(sol.plusOne([1, 2, 9, 2, 2, 9]))
