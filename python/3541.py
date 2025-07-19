from collections import Counter
from typing import Dict


class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = "aeiou"
        letters = "bcdfghjklmnpqrstvwxyz"
        counter = Counter(s)
        vowels_dict: Dict[str, int] = {}
        letters_dict: Dict[str, int] = {}
        for key, value in counter.items():
            if key in vowels:
                vowels_dict[key] = value
            elif key in letters:
                letters_dict[key] = value
        if vowels_dict == {}:
            return max(letters_dict.values())
        elif letters_dict == {}:
            return max(vowels_dict.values())
        return max(vowels_dict.values()) + max(letters_dict.values())


sol = Solution()
print(sol.maxFreqSum(s="aeiaeia"))
