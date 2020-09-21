class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        a, b = Counter(A.split()), Counter(B.split())
        uncommon = lambda d1, d2: [i for i in d1 if i not in d2 and d1[i] == 1]
        return uncommon(a, b) + uncommon(b, a)
