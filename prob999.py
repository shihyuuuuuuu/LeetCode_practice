class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        find, ans = False, 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "R":
                    m, n = i, j
                    find = True
                    break
            if find:
                break
        for i in range(m-1, -1, -1):
            if board[i][n] == "p":
                ans += 1
                break
            elif board[i][n] == "B":
                break
        for i in range(m+1, 8):
            if board[i][n] == "p":
                ans += 1
                break
            elif board[i][n] == "B":
                break
        for j in range(n-1, -1, -1):
            if board[m][j] == "p":
                ans += 1
                break
            elif board[m][j] == "B":
                break
        for j in range(n+1, 8):
            if board[m][j] == "p":
                ans += 1
                break
            elif board[m][j] == "B":
                break
        return ans
