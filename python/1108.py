class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = address.replace(".", "[.]")
        return "".join(res)


sol = Solution()
print(sol.defangIPaddr("1.1.1.1"))
