class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            digits = 0
            while i != 0:
                i //= 10
                digits += 1
            if not digits & 1:
                ans += 1
        return ans
