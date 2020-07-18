class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in A:
            ans.append([1 ^ j for j in i[::-1]])
        return ans
