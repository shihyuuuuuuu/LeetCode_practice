class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        matrix = []
        for i in range(n):
            matrix.append([0] * m)
        for i in indices:
            for j in range(m):
                matrix[i[0]][j] += 1
            for j in range(n):
                matrix[j][i[1]] += 1
        ans = 0
        for i in matrix:
            for j in i:
                if j & 1:
                    ans += 1
        return ans
