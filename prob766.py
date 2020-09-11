class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for j in range(n - 1, -1, -1):
            ele = None
            for i in range(m):
                if ele == None:
                    ele = matrix[i][j]
                elif ele != matrix[i][j]:
                    return False
                j += 1
                if j == n:
                    break
        for i in range(1, m):
            ele = None
            for j in range(n):
                if ele == None:
                    ele = matrix[i][j]
                elif ele != matrix[i][j]:
                    return False
                i += 1
                if i == m:
                    break
        return True
