class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        ans = 0
        x = abs(x)
        l = []
        while x > 0:
            l.append(x % 10)
            x //= 10
        for index, i in enumerate(l[::-1]):
            ans += i*10**index
        ans *= sign
        return 0 if ans > 2**31-1 or ans < -2**31 else ans
