from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        char_indexes = []
        for i in range(len(s)):
            got_index = s.find(c, i)
            if got_index not in char_indexes and got_index != -1:
                char_indexes.append(got_index)
        result = []
        s_len = len(s)
        for i in range(s_len):
            count = 0
            temp = []
            if s[i] == c:
                result.append(0)
                continue
            while count < len(char_indexes):
                temp.append(abs(i - char_indexes[count]))
                count += 1
                print(temp)
            result.append(min(temp))
        return result


sol = Solution()
print(sol.shortestToChar(s="aaba", c="b"))
