class Solution:
    def climbStairs(self, n: int) -> int:
        x, y = 0, 1
        for i in range(1, n+1):
            x, y = y, x+y
        return y
        
        # Time Limit Exceeded
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)
