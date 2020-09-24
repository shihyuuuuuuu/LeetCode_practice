class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(1)
        for i in nums[:-1]:
            if i < 0:
                i = -1 * (i + 1)
            nums[i] = -(nums[i]+1)
        for cnt, i in enumerate(nums):
            if i >= 0:
                return cnt

        # 其實可以用 sum，算總和差了多少
