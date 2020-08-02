class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for cnt, i in enumerate(A):
            if i in A[:cnt]:
                return i
