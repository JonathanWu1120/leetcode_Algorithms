class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0 or num == 1:
            return True
        x = 1
        y = 0
        while num > y:
            y += x
            x += 2
        return num == y