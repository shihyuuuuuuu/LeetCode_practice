class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in grid:
            ans += max(i)
            ans += sum([1 if j else 0 for j in i])
        for j in range(len(grid[0])):
            ans += max([grid[i][j] for i in range(len(grid))])
        return ans
