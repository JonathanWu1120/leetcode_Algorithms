class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 0 or len(prices) == 1:
            return 0
        diff = prices[0]
        max = diff
        c = 0
        for i in prices:
            if i > max:
                c = i - max
                max = i
            if i < diff:
                diff = i
            if (i - diff) > c:
                c = i - diff
        return c
