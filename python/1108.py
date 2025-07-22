class Solution:
    def defangIPaddr(self, address: str) -> str:
        address_list = list(address)
        res = []
        for char in address_list:
            if char == ".":
                res.append("[")
                res.append(".")
                res.append("]")
            else:
                res.append(char)
        return "".join(res)


sol = Solution()
print(sol.defangIPaddr("1.1.1.1"))
