class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for num, idx in zip(nums, index):
            if idx <= len(target):
                target = target[:idx] + [num] + target[idx:]
            else:
                target.append(num)
        return target
