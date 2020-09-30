class Solution:
    def bitwiseComplement(self, N: int) -> int:
        n = N
        mask = 0
        while n:
            n >>= 1
            mask = (mask << 1) | 1
        return 1 if not N else ~N & mask
