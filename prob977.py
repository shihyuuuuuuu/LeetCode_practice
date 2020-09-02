class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        #A = [i**2 for i in A]
        #A.sort()
        #return A
        
        left = 0
        right = len(A) - 1
        ans = []
        while left <= right:
            if abs(A[left]) < abs(A[right]):
                ans.append(A[right]**2)
                right -= 1
            else:
                ans.append(A[left]**2)
                left += 1
        return ans[::-1]
