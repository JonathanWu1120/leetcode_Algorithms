class Solution(object):
    def mkd(self,s):
        arr = {}
        for c in s:
            if c not in arr:
                arr[c] = 1
            elif c in arr:
                arr[c] += 1
        return arr
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = self.mkd(s)
        a = 0
        o = False
        for k,v in arr.items():
            if v % 2 == 0:
                a += v
            else:
                if v > 1:
                    a += v - 1
                o = True
        if o == True:
            a += 1
        return a