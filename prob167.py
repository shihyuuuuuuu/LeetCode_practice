class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while True:
            tmp = numbers[l] + numbers[r] - target
            if tmp == 0:
                return [l+1, r+1]
            elif tmp < 0:
                l += 1
            else:
                r -= 1
                
