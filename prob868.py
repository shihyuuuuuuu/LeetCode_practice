class Solution:
    def binaryGap(self, N: int) -> int:
        dist, cnt = 0, -1
        while N & 1 == 0:
            N >>= 1
        while N > 0:
            cnt += 1
            if N & 1:
                dist = max(dist, cnt)
                cnt = 0
            N >>= 1
        return dist
