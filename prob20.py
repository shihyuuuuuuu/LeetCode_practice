class Solution:
    def isValid(self, s: str) -> bool:
        open_brac = { '(': 0, '{': 1, '[': 2 }
        close_brac = { ')': 0, '}': 1, ']': 2 }
        open_stack = [-1]
        for i in s:
            if i in open_brac:
                open_stack.append(open_brac[i])
            else:
                if open_stack[-1] == close_brac[i]:
                    open_stack.pop()
                else:
                    return False
        return False if open_stack[-1] != -1 else True
