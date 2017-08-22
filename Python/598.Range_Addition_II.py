class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if ops == []:
            return(m*n)
        a,b = float("inf"), float("inf")
        for i in ops:
            if i[0] < a:
                a = i[0]
            if i[1] < b:
                b = i[1]
        return a*b