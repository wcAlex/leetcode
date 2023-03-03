class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        curLowest, maxGain = float('inf'), 0
        for price in prices:
            if price < curLowest:
                curLowest = price
            
            if price - curLowest > maxGain:
                maxGain = price - curLowest

        return maxGain