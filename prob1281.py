class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        _sum = 0
        while n != 0:
            x = n % 10
            n //= 10
            product *= x
            _sum += x
        return product - _sum
