class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = {}
        for i in arr:
            cnt[i] = cnt.get(i, 0) + 1
        lucky = [i for i in cnt if i == cnt[i]]
        return max(lucky) if lucky else -1
        
        # Using built-in functions
        cnt = Counter(arr).most_common()
        for i in cnt:
            if i[0] == i[1]:
                return i[0]
        return -1
