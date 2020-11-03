class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        flatten = [j for i in grid for j in i]
        k %= len(flatten)
        flatten = flatten[-k:] + flatten[:-k]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = flatten.pop(0)
        return grid
