class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mad = []
        mini = 1000002
        for i in range(len(arr)-1):
            diff = abs(arr[i] - arr[i+1])
            if diff <= mini:
                if diff < mini:
                    mad = []
                    mini = diff
                mad.append([arr[i], arr[i+1]])
        return mad
