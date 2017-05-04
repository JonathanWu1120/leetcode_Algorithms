class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 0 or len(prices) == 1:
            return 0
        diff = prices[0]
        max = diff
        profit = 0
        total = 0
        for i in prices:
            if i > max:
                max = i
            if i - diff > profit:
                profit = i - diff
            if i < max:
                #print(i,total,profit,max,diff)
                total += profit
                max = i
                diff = max
                profit = 0
                #print(i,total,profit,max,diff)
        total += profit
        return total