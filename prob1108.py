class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ""
        for i in address:
            ans += i if i != '.' else '[.]'
        return ans
