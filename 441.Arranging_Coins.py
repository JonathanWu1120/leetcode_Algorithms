class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        row = 0
        while n > row:
            row += 1
            n -= row
        return row