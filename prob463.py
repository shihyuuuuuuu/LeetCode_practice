class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        overlap = land = 0
        m = len(grid) - 1
        n = len(grid[0]) - 1
        for row, i in enumerate(grid):
            for col, j in enumerate(i):
                if j:
                    land += 1
                    if row < m:
                        if grid[row+1][col]:
                            overlap += 1
                    if col < n:
                        if grid[row][col+1]:
                            overlap += 1
        return 4 * land - 2 * overlap
