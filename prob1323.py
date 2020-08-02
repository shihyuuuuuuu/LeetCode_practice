class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = []
        ans = 0
        first_i = True
        while num > 0:
            digits.append(num % 10)
            num //= 10
        for cnt, i in enumerate(digits[::-1]):
            if i == 6 and first_i:
                i = 9
                first_i = False
            ans += i * 10**(len(digits)-1-cnt)
        return ans
