class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Using additional space
        cnt = [0] * len(nums)
        for i in nums:
            cnt[i-1] += 1
        return [x+1 for x, i in enumerate(cnt) if i == 0]
        
        # O(1) running time without extra space
        for i in nums:
            if nums[abs(i)-1] > 0:
                nums[abs(i)-1] *= -1
        return [cnt+1 for cnt, i in enumerate(nums) if i > 0]
