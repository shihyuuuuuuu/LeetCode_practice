class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
    
        lowest = highest = prices[0]
        profit = 0
        for i in prices[1:]:
            if i < lowest:
                lowest = highest = i
            elif i > highest:
                highest = i
                profit = max(profit, highest - lowest)
        return profit
    
        # Another Solution
        profit, lowest = 0, float("inf")
        for i in prices:
            if i < lowest:
                lowest = i
            else:
                profit = max(profit, i - lowest)
        return profit
