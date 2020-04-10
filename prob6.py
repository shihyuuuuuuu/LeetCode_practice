class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        arr = []
        direction = 1
        row = 0
        ans = ""
        for i in range(numRows):
            arr.append([])
        for i in range(len(s)):
            arr[row].append(s[i])
            row += direction
            if row == numRows-1:
                direction = -1
            if row == 0:
                direction = 1
        for i in arr:
            for j in range(len(i)):
                ans += i[j]
        return ans
