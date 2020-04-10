class Solution:
    """
    def getStrIndex(self, s, i):
        return s[i]
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = ""
        for i in range(min(map(len, strs))):
            if len(set(list(map(self.getStrIndex, strs,  [i]*len(strs))))) == 1:
                ans += strs[0][i]
            else:
                break
        return ans
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for index, s in enumerate(shortest):
            for c in strs:
                if c[index] != s:
                    return shortest[:index]
        return shortest
