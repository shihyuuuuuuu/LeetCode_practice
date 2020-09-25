class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = 0
        last_idx = 0
        idx = -1
        for cnt, i in enumerate(arr):
            if i == 0:
                zeros += 1
            if cnt + zeros == len(arr)-1:
                last_idx = cnt
                break
            if cnt + zeros == len(arr):
                last_idx = cnt - 1
                idx = -2
                arr[-1] = 0
                break
            
        for i in arr[last_idx::-1]:
            arr[idx] = i
            idx -= 1
            if i == 0:
                arr[idx] = i
                idx -= 1
