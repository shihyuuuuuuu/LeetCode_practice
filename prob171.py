class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for cnt, i in enumerate(s[::-1]):
            ans += (ord(i) - 64) * pow(26, cnt)
        return ans
        
        # Or in one line
        return sum((ord(i) - 64) * pow(26, cnt) for cnt, i in enumerate(s[::-1]))
