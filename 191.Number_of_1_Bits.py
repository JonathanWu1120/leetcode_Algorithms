class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = "{0:b}".format(n)
        a = 0
        for i in n:
            if i == "1":
                a += 1
        return a
        