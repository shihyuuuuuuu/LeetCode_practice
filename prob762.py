class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        # Because 1000000 has 20 bits in binary, so the possible prime numbers are from 2 to 19
        return sum(1 if bin(i).count('1') in [2, 3, 5, 7, 11, 13, 17, 19] else 0 for i in range(L, R+1))
