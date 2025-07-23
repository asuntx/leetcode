from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score: List[int] = []
        for operation in operations:
            if operation == "C":
                score.pop()
            elif operation == "+":
                score.append(score[-2] + score[-1])
            elif operation == "D":
                score.append(score[-1] * 2)
            elif isinstance(int(operation), int):
                score.append(int(operation))
                print(score)

        return sum(score)


sol = Solution()
print(sol.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
