class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        for index, i in enumerate(nums):
            if i == val:
                cnt += 1
            else:
                nums[index-cnt] = i
        return len(nums) - cnt
