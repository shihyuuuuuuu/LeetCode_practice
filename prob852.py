class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for index, i in enumerate(A[1:-1]):
            if A[index] < i > A[index+2]:
                return index+1
