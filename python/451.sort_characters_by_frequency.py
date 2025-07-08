from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        sorted_dict = dict(sorted(Counter(s).items(), key=lambda x: x[1], reverse=True))
        response = ""
        for char in sorted_dict:
            while sorted_dict[char] > 0:
                response += char
                sorted_dict[char] -= 1
        return response


sol = Solution()
print(sol.frequencySort("loveleetcode"))
