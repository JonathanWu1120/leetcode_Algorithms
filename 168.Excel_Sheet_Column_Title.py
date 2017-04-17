class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        arr = {}
        a = ""
        for i in range(65,91):
            arr[i-65] = chr(i)
        while n > 0:
            x = (n-1)%26
            if x == 0:
                a += arr[0]
            else:
                a += arr[x]
            n -= x
            n /= 26
        return a[::-1]