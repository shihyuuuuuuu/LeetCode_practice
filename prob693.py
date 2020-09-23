class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = bin(n)
        for cnt, i in enumerate(b[1:-1]):
            if i == b[cnt+2]:
                return False
        return True
