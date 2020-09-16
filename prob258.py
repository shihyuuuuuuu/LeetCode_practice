class Solution:
    def addDigits(self, num: int) -> int:
        # Find the regular pattern
        return 0 if num == 0 else num % 9 if num % 9 else 9
    
        # Traditional Solution
        while num >= 10:
            tmp = 0
            while num:
                tmp += num % 10
                num //=10
            num = tmp
        return num
