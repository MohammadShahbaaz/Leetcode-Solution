class Solution(object):
    def maxProfit(self, prices):
        l = prices[0]
        g = 0
        for i in range(len(prices)):
            if prices[i] < l:
                l = prices[i]
            p = prices[i] - l
            
            if p>g:
                g = p 
            
        return g