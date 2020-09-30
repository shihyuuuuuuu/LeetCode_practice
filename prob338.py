class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]
        j = 0
        for i in range(1, num+1):
            #if math.log(i, 2) == int(math.log(i, 2)):
            if i & (i-1) == 0:
                j = 0
            ans.append(ans[j]+1)
            j += 1
        return ans
"""
0
1
10
11
100
101
110
111
1000
1001
1010
1011
1100
1101
1110
1111
"""
# 0  1  1 2  1 2 2 3  1 2 2 3 2 3 3 4

