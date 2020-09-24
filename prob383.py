class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r, m = Counter(ransomNote), Counter(magazine)
        for i in r:
            if r[i] > m.get(i, 0):
                return False
        return True
