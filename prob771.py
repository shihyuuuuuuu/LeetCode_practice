class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        ans = 0
        for c in S:
            if c in J:
                ans += 1
        return ans
    
        # Other solution
        return sum(map(J.count, S))
        # or
        return sum(map(S.count, J))
