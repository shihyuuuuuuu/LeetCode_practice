class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        rank_idx = [i for _, i in sorted(zip(nums, range(0, len(nums))), reverse=True)]
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i) for i in range(4, len(nums)+1)]
        return [i for _, i in sorted(zip(rank_idx, ranks))]
