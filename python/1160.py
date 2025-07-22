from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        good_words: List[str] = []
        chars_counter = Counter(chars)
        for word in words:
            word_counter = Counter(word)
            add: bool = True
            for char in word:
                if char not in chars:
                    add = False
                    break
                if not word_counter[char] <= chars_counter[char]:
                    add = False
                    break
            if add:
                good_words.append(word)
        return len("".join(good_words))


sol = Solution()
print(sol.countCharacters(["cat", "bt", "hat", "tree"], "atach"))
