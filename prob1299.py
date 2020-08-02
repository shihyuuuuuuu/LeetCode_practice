class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        r_max = max(arr)
        for i in range(len(arr)-1):
            if arr[i] == r_max:
                r_max = max(arr[i+1:])
            ans.append(r_max)
        ans.append(-1)
        return ans
