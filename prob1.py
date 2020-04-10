class Solution:
    # Faster, more memory
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for idx, i in enumerate(nums):
            num_dict[i] = idx
            
        for idx, i in enumerate(nums):
            if((target - i) in num_dict and num_dict[target-i] != idx):
                return [idx, num_dict[target-i]]
            
    # Slower, less memory
    def twoSum_ver2(self, nums: List[int], target: int) -> List[int]:
        for idx1, i in enumerate(nums):
            for idx2, j in enumerate(nums[idx1+1:]):
                if(i + j == target):
                    return [idx1, idx1+idx2+1]
                
