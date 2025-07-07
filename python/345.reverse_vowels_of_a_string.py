class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        n = list(s)
        start = 0
        end = len(s) - 1
        while start < end:
            while start < end and vowels.find(n[start]) == -1:
                start += 1
            while start < end and vowels.find(n[end]) == -1:
                end -= 1
            n[start], n[end] = n[end], n[start]
            start += 1
            end -= 1
        return "".join(n)


sol = Solution()
print(sol.reverseVowels("IceCreAm"))
