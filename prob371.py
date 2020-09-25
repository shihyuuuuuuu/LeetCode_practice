class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF # Limit the length into 32-bit
        MAX = 0x8FFFFFFF # Max Integer in 32-bit
        def add(a, b):
            if b == 0:
                return a 
            s = (a ^ b) & mask # calculate sum without carry
            c = ((a & b) << 1) & mask # calculate carry
            return add(s, c)
        ans = add(a, b)
        return ans if ans <= 0x8FFFFFFF else ~(ans ^ mask) # ~x = -x-1
    
    # Ref: https://hackmd.io/@sysprog/c-numerics?type=view%EF%BC%8C
