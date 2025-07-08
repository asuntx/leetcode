from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        first_word_count = Counter(words[0])
        for word in words[1:]:
            temp_count = Counter(word)
            for item in first_word_count:
                if item in temp_count:
                    if temp_count[item] < first_word_count[item]:
                        first_word_count[item] = temp_count[item]
                else:
                    first_word_count[item] = 0
        response = []
        for char in first_word_count:
            while first_word_count[char] != 0:
                response.append(char)
                first_word_count[char] -= 1
        return response


sol = Solution()
print(sol.commonChars(["bella", "label", "roller"]))
