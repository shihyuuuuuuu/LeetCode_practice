class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, curr, c, ans = 0, 0, s[0], 0
        for i in s:
            if i != c:
                prev = curr
                curr = 0
                c = i
            curr += 1
            if curr <= prev:
                ans += 1
        return ans
