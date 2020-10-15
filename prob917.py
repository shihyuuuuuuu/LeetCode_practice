class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        ans = [' '] * len(S)
        for i in range(len(S)):
            if not S[i].isalpha():
                ans[i] = S[i]
        ptr = -1
        for i in range(len(S)):
            if S[i].isalpha():
                while ans[ptr] != ' ':
                    ptr -= 1
                ans[ptr] = S[i]
        return ''.join(ans)
