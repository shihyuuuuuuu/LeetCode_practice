class Solution:
    def sortString(self, s: str) -> str:
        cnt = [0 for i in range(26)]
        for i in s:
            cnt[ord(i) - 97] += 1
        freq = []
        for i in range(26):
            if cnt[i]:
                freq.append([chr(i+97), cnt[i]])
        end = False
        ans = ""
        while not end:
            for i in range(len(freq)):
                if freq[i][1]:
                    ans += freq[i][0]
                    freq[i][1] -= 1
            for i in range(len(freq)-1, -1, -1):
                if freq[i][1]:
                    ans += freq[i][0]
                    freq[i][1] -= 1
            end = True
            for i in freq:
                if i[1]:
                    end = False
                    break
        return ans
