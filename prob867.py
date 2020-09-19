class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        ans = [[] for i in range(len(A[0]))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                ans[j].append(A[i][j])
        return ans
