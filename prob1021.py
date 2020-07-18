class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ans = ""
        cnt = left = 0
        for index, i in enumerate(S):
            cnt += 1 if i == '(' else -1
            if cnt == 0:
                ans += S[left+1:index]
                left = index + 1
        return ans
