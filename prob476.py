class Solution:
    def findComplement(self, num: int) -> int:
        ans = power = 0
        while num != 0:
            c = (num % 2) ^ 1
            num //= 2
            ans += c * 2**power
            power += 1
        return ans
