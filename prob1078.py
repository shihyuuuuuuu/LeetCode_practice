class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        t = text.split()
        if len(t) < 3:
            return []
        return [t[i] for i in range(2, len(t)) if t[i-2] == first and t[i-1] == second]
