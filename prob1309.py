class Solution:
    def freqAlphabets(self, s: str) -> str:
        cnt = len(s) - 1
        ans = ""
        while cnt >= 0:
            if s[cnt] != "#":
                ans = chr(int(s[cnt]) + 96) + ans
                cnt -= 1
            else:
                ans = chr(int(s[cnt-2:cnt]) + 96) + ans
                cnt -= 3
        return ans
