class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        for s in s.split():
            ans += s[::-1] + ' '
        return ans[:-1]
