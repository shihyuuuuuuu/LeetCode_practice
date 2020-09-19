class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = Counter(chars)
        ans = 0
        for i in words:
            tmp = Counter(i)
            success = True
            for j in tmp:
                if j in cnt:
                    if tmp[j] > cnt[j]:
                        success = False
                        break
                else:
                    success = False
                    break
            if success:
                ans += len(i)
        return ans
