class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gptr = 0
        while s and gptr < len(g):
            if s[0] >= g[gptr]:
                gptr += 1
            s.pop(0)
        return gptr
