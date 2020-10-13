class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        a_diff = (sum(B) - sum(A)) // 2
        mapping = {}
        for a in A:
            mapping[a_diff + a] = a
        for b in B:
            if b in mapping:
                return [mapping[b], b]
