class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for letter in s:
            number += romans[letter]
        return number


sol = Solution()
print(sol.romanToInt(s="CIV"))
