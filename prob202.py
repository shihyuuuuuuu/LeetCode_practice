class Solution:
    def isHappy(self, n: int) -> bool:
        arr = []
        while n != 1:
            s = 0
            while n > 0:
                s += (n % 10)**2
                n //= 10
            if s in arr:
                return False
            else:
                arr.append(s)
            n = s
        return True
