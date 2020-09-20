"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        #return [[i, j] for i in range(1,1001) for j in range(1,1001) if customfunction.f(i, j) == z]
        ans = []
        for i in range(1, 1001):
            haveToBreak = False
            for j in range(1, 1001):
                Z = customfunction.f(i, j)
                if Z == z:
                    ans.append([i, j])
                elif Z > z:
                    if j == 1:
                        haveToBreak = True
                    break
            if haveToBreak:
                break
        return ans
