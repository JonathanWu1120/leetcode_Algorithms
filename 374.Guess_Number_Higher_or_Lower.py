# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = n
        while True:
            x = guess(a)
            n -= n//2
            if x == 0:
                return a
            elif x == 1:
                a += n
            elif x == -1:
                a -= n