class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # One line solution
        return len([j for i in grid for j in i if j < 0])
        
        ans = 0
        l = len(grid[0])
        for i in grid:
            for cnt, j in enumerate(i):
                if j < 0:
                    ans += l - cnt
                    break
        return ans
