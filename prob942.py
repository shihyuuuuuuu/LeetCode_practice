class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        l, r, ans = 0, len(S), []
        for i in S:
            if i == 'I':
                ans.append(l)
                l += 1
            elif i == 'D':
                ans.append(r)
                r -= 1
        ans.append(ans[-1]-1 if S[-1] == 'D' else ans[-1]+1)
        return ans
