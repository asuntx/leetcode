from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        n1, n2 = s1.split(), s2.split()
        all_words = n1 + n2
        word_count = Counter(all_words)
        return [word for word in word_count if word_count[word] == 1]


sol = Solution()
print(sol.uncommonFromSentences("s z z z s ju x z z", "z tt zz ss s t w ejt"))
