class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        a = "{0:b}".format(z)
        b = 0
        for i in a:
            if i == "1":
                b += 1
        return b