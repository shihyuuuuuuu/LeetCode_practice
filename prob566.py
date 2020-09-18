class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums
        ans = [[]]
        R, C = 0, 0
        for i in nums:
            for j in i:
                if C == c:
                    C = 0
                    R += 1
                    ans.append([])
                ans[R].append(j)
                C += 1
        return ans
    
        # Or use // and %
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums
        ans = []
        R = 0
        while R < r:
            ans.append([nums[(i+c*R)//n][(i+c*R)%n] for i in range(c)])
            R += 1
        return ans
