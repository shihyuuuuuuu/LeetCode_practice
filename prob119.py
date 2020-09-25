class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(rowIndex):
            row = list(map(lambda x, y: x + y, [0] + row, row + [0]))
        return row
