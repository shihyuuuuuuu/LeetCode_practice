class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = 0
        ans = 0
        for c in s:
            cnt += 1 if c == 'R' else -1
            if cnt == 0:
                ans += 1
        return ans
