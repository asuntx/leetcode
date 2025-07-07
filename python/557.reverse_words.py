class Solution:
    def reverseWords(self, s: str) -> str:
        def reverseWord(word: str) -> str:
            return word[::-1]

        words = s.split(" ")
        n = []
        for word in words:
            n.append(reverseWord(word))
        return " ".join(n)


sol = Solution()
print(sol.reverseWords(". ., ,"))
