class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smaller_cnt = 0
        ans = []
        prev = -1
        sorted_idx = sorted(range(len(nums)), key=lambda k: nums[k])
        nums.sort()
        for index, i in enumerate(nums):
            if i == prev:
                ans.append(smaller_cnt)
            else:
                smaller_cnt = index
                ans.append(smaller_cnt)
            prev = i
        real_ans = [None] * len(ans)
        for i, j in zip(sorted_idx, ans):
            real_ans[i] = j
        return real_ans
        
        # One line solution
        return [*map(sorted(nums).index, nums)]
