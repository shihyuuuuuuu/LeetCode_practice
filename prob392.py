class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        tptr = 0
        for i in s:
            if tptr < len(t):
                while t[tptr] != i:
                    tptr += 1
                    if tptr == len(t):
                        return False
                tptr += 1
            else:
                return False
        return True
