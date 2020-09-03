class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        ans = 0
        for j in range(len(A[0])):
            for i in range(len(A)-1):
                if A[i][j] > A[i+1][j]:
                    ans += 1
                    break
        return ans
