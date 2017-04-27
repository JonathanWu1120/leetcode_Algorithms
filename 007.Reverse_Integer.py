class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = str(x)[::-1]
        x = False
        if "-" in a:
            a = int(a[:-1])
            x = True
        else:
            a = int(a)
        if a < 2147483647 and a > -2147483647:
            if x == True:
                return 0 - a
            return a
        return 0