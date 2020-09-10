class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        ans = [-1] * len(A)
        even, odd = 0, 1
        for i in A:
            if i & 1:
                ans[odd] = i
                odd += 2
            else:
                ans[even] = i
                even += 2
        return ans
    
        # Another solution
        idx = [[], []]
        for cnt, i in enumerate(A):
            if (cnt & 1) ^ (i & 1):
                idx[cnt & 1].append(cnt)
        for i in range(len(idx[0])):
            A[idx[0][i]] = A[idx[0][i]] + A[idx[1][i]]
            A[idx[1][i]] = A[idx[0][i]] - A[idx[1][i]]
            A[idx[0][i]] = A[idx[0][i]] - A[idx[1][i]]
        return A
