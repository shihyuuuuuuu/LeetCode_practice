class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # By sort
        s = sorted(s)
        t = sorted(t)
        if len(s) < len(t):
            s += chr(125) # 97+26
        else:
            t += chr(125)
        for i, j in zip(s, t):
            if i != j:
                return min(i, j)
            
        # By counter
        s = Counter(s)
        t = Counter(t)
        big, small = (s, t) if len(s) > len(t) else (t, s)
        for i in big:
            if i not in small:
                return i
            if big[i] != small[i]:
                return i
