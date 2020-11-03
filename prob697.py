class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = {}
        max_deg = 0
        min_len = float('inf')
        for idx, i in enumerate(nums):
            d[i] = d.get(i, {'start': idx, 'degree': 0})
            d[i]['len'] = idx - d[i]['start'] + 1
            d[i]['degree'] += 1
            if d[i]['degree'] > max_deg:
                max_deg, min_len = d[i]['degree'], d[i]['len']
            elif d[i]['degree'] == max_deg:
                min_len = min(min_len, d[i]['len'])
        return min_len
