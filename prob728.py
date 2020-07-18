class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1):
            self_dividing = True
            for j in str(i):
                if j == '0':
                    self_dividing = False
                    break
                if i % int(j):
                    self_dividing = False
                    break
            if self_dividing:
                ans.append(i)
        return ans
