class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        co, dist = [], []
        for i in range(R):
            for j in range(C):
                co.append([i, j])
                dist.append(abs(i-r0) + abs(j-c0))
        return [i for _, i in sorted(zip(dist, co))]
        
        # Another solution by key
        matrix = [(r, c) for r in range(R) for c in range(C)]
        
        return sorted(matrix, key=lambda cell: abs(cell[0] - r0) + abs(cell[1] - c0))
