class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse = True)
        half = sum(nums) / 2
        tmp, ans = 0, []
        for i in nums:
            tmp += i
            ans.append(i)
            if tmp > half:
                break
        return ans
