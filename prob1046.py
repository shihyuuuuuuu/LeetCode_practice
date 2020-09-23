class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            add = [stones[-1] - stones[-2]] if stones[-1] - stones[-2] > 0 else []
            stones.pop()
            stones.pop()
            stones += add
        return sum(stones)
