class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        last_lowest = prices[0]
        profit = 0
        for i in prices[1:]:
            if i >= last_lowest:
                profit += i - last_lowest
            last_lowest = i
        return profit
