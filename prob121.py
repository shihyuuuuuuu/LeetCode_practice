class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        low = high = prices[0]
        diff = 0
        for i in prices[1:]:
            if i < low:
                low = i
                high = i
            elif i > high:
                high = i
                if high - low > diff:
                    diff = high - low
        return diff
