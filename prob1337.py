class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Using "zip"
        return [i for _, i in sorted(zip([sum(i) for i in mat], list(range(len(mat)))))][:k]
    
        # Using "key"
        return sorted(list(range(len(mat))), key=lambda x: (sum(mat[x]), x))[:k]
