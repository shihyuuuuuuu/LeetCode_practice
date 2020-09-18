class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        for i in arr2:
            ans += [i] * arr1.count(i)
        return ans + sorted([i for i in arr1 if i not in arr2])
    
        # Another solution by sorting two lists
        pos = {}
        for i in range(len(arr2)):
            pos[arr2[i]] = i
        arr1_pos = [pos[i] if i in pos else 1001 for i in arr1]
        return [i for _, i in sorted(zip(arr1_pos, arr1))]
        
        # Reference:
        # 1. https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
        # 2. https://stackoverflow.com/questions/9764298/how-to-sort-two-lists-which-reference-each-other-in-the-exact-same-way
