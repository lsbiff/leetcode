#sliding window technique
class Solution:
    def maxProfit(self, prices) -> int:

        maxValue = 0
        buy = 0
        sell = 1
        
        while sell < len(prices):

            if prices[buy] < prices[sell]:
                myProfit = prices[sell] - prices[buy]
                maxValue = max(maxValue, myProfit)        
            else:
                buy = sell

            sell = sell + 1
               
                  
        return maxValue

print(Solution.maxProfit(None, [2,4,1]))