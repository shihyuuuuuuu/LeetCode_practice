class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        wptr = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[wptr] = nums[i]
                wptr += 1
        return wptr
