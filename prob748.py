class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        mini_len = float("inf")
        lic_dict = Counter([i.lower() for i in licensePlate if i.isalpha()])
        ans = None
        for i in words:
            c = Counter(i)
            if all(lic_dict[j] <= c.get(j, -1) for j in lic_dict):
                if len(i) < mini_len:
                    ans = i
                    mini_len = len(i)
        return ans
