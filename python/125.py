from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        temp: List[str] = []
        for char in s:
            if char.isalnum():
                temp.append(char)
        if temp == []:
            return True
        alnum_s: str = "".join(temp).lower()
        i = 0
        j = len(alnum_s) - 1
        if alnum_s[i] != alnum_s[-1]:
            return False
        for char in alnum_s:
            if alnum_s[i] != alnum_s[j]:
                return False
            if i == len(alnum_s) - 1:
                break
            i += 1
            j -= 1
        return True


sol = Solution()
print(sol.isPalindrome(s="."))
