class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        temp = s.split()
        s_index = {}
        pattern_index = {}
        if len(pattern) != len(temp):
            return False
        for i in range(len(temp)):
            if pattern[i] not in pattern_index:
                pattern_index[pattern[i]] = i
            if temp[i] not in s_index:
                s_index[temp[i]] = i
            if s_index[temp[i]] != pattern_index[pattern[i]]:
                return False
        return True


sol = Solution()
print(sol.wordPattern("abbaba", "dog cat cat dog cat dog"))
