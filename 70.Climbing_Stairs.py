class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        a = 1
        b = 1
        while n > 1:
            c = a + b
            a = b 
            b = c
            n -= 1
        return c