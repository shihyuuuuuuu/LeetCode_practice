class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(text)
        return min(cnt['b']//1, cnt['a']//1, cnt['l']//2, cnt['o']//2, cnt['n']//1)
