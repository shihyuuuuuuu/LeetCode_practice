class Solution:
    def judgeCircle(self, moves: str) -> bool:
        v = h = 0
        for i in moves:
            if i in ('R', 'L'):
                h += 1 if i == 'R' else -1
            elif i in ('U', 'D'):
                v += 1 if i == 'U' else -1
        return True if v == h == 0 else False
    
        # Another solution (faster)
        return moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D')
