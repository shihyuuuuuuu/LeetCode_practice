class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        N = len(grid)
        overlapped = cubes = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j]:
                    if j < N-1:
                        overlapped += min(grid[i][j], grid[i][j+1]) * 2
                    if i < N-1:
                        overlapped += min(grid[i][j], grid[i+1][j]) * 2
                    overlapped += (grid[i][j] - 1) * 2
                    cubes += grid[i][j]
        return cubes * 6 - overlapped
