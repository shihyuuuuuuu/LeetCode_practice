class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        for index, i in enumerate(A):
            if not(i & 1):
                A.insert(0, A.pop(index))
        return A
    
        # another solution
        return [i for i in A if not(i&1)] + [i for i in A if i&1]
