class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt, M = 0, 0
        for i in nums:
            if i:
                cnt += 1
                M = max(cnt, M)
            else:
                cnt = 0
        return M

        # Another cool solution on the web:
        for i in range(1, len(nums)):
            if nums[i]:
                nums[i] += nums[i - 1]
        return max(nums)
