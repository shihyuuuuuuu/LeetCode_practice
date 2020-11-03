class Solution:
    def countLargestGroup(self, n: int) -> int:
        group = [0] * 36
        for i in range(1, n+1):
            s = 0
            while i > 0:
                s += i % 10
                i //= 10
            group[s-1] += 1
        return group.count(max(group))
