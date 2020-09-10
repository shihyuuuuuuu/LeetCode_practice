class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        c_index, ans = [], []
        for i in range(len(S)):
            if S[i] == C:
                c_index.append(i)
        for i in range(len(S)):
            min_dist = 10000
            for j in c_index:
                min_dist = min(min_dist, abs(j - i))
            ans.append(min_dist)
        return ans
