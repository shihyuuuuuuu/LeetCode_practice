class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        smaller = [A[i] < A[i+1] for i in range(len(A)-1) if A[i] != A[i+1]]
        return all(smaller) == True or any(smaller) == False
