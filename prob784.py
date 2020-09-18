class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def search(cur, ptr, ans):
            if ptr == len(S):
                ans.append(cur)
                return
            new_ptr = ptr
            while S[new_ptr].isdigit():
                new_ptr += 1
                if new_ptr == len(S):
                    ans.append(cur+S[ptr:new_ptr])
                    return
            cur += S[ptr:new_ptr]
            search(cur+S[new_ptr].lower(), new_ptr+1, ans)
            search(cur+S[new_ptr].upper(), new_ptr+1, ans)
        ans = []
        ptr = 0
        cur = ""
        search(cur, ptr, ans)
        return ans
