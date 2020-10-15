class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        l = sum([cnt[i]-1 if cnt[i] & 1 else cnt[i] for i in cnt])
        return l + 1 if len(s) > l else l
