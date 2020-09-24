class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i, j in zip(x[:len(x)//2], x[::-1][:len(x)//2]):
            if i != j:
                return False
        return True

        # One-liner
        return str(x) == str(x)[::-1]

        # Solution from the discussion
        if x < 0:
            return False
        a = 1
        while x / (10*a) > 1:
            a *= 10
        while x:
            high = x // a
            low = x % 10
            if high != low:
                return False
            x = (x % a) // 10
            a //= 100
        return True
