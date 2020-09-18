class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = "A"
        for i in S:
            if stack[-1] != i:
                stack += i
            else:
                stack = stack[:-1]
        return stack[1:]
