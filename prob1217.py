class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = even = 0
        for i in position:
            if i & 1:
                odd += 1
            else:
                even += 1
        return min(odd, even)
