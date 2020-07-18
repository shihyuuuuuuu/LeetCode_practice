class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = {}
        for i in nums:
            cnt[i] = 2 if i in cnt else 1
        for i in cnt:
            if cnt[i] == 1:
                return i
