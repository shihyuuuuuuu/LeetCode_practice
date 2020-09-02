class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for i in range(1, n, 2):
            ans += [i, -i]
        return ans + [0] if n & 1 else ans
