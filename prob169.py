class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_cnt = {}
        half = len(nums) // 2
        for i in nums:
            if i not in num_cnt:
                num_cnt[i] = 1
            else:
                num_cnt[i] += 1
            if num_cnt[i] > half:
                return i
