class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long_seq = ""
        max_len = 0
        for i in range(len(s)):
            if s[i] not in long_seq:
                long_seq += s[i]
                max_len = max(len(long_seq), max_len)
            else:
                long_seq = long_seq[long_seq.index(s[i])+1:] + s[i]
        return max_len
