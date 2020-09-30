class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # O(M*N) time complexity, O(1) extra memory
        cnt = 0
        m, n = len(board), len(board[0])
        for i in range(m):
            ishorizon = False
            for j in range(n):
                if board[i][j] == '.':
                    ishorizon = False
                elif board[i][j] == 'X':
                    if not ishorizon:
                        if i > 0:
                            if board[i-1][j] == 'X':
                                continue
                        cnt += 1
                        ishorizon = True
        return cnt
        
        
        # Original complex and slow solution
        def search_ship(i, j):
            while i < self.m - 1:
                if board[i+1][j] == '.':
                    break
                else:
                    self.ships.append([i+1, j])
                    i += 1
            while j < self.n - 1:
                if board[i][j+1] == '.':
                    break
                else:
                    self.ships.append([i, j+1])
                    j += 1
        cnt = 0
        self.ships = []
        self.m = len(board)
        self.n = len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == 'X':
                    if [i, j] not in self.ships:
                        cnt += 1
                        self.ships.append([i, j])
                        search_ship(i, j)
        return cnt
