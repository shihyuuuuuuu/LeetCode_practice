class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ans = []
        for i in range(len(A)):
            A[i] = Counter(A[i])
        for i in A[0]:
            cnt = A[0][i]
            for j in A:
                cnt = min(cnt, j[i])
            ans += [i] * cnt
        return ans
