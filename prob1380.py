class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        row_min = [min(i) for i in matrix]
        col_max = [max(matrix[i][j] for i in range(m)) for j in range(n)]
        return list(set(row_min).intersection(set(col_max)))
        
        # Or write them in one line
        return list(set([min(i) for i in matrix]).intersection(set([max(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0]))])))
