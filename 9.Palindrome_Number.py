class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        w = str(x)
        i = 0
        j = len(w) - 1
        k = len(w)/2
        pal = True
        while pal and i < k:
            if w[i] == w[j]:
                pal = True
                i += 1
                j -= 1
            else:
                pal = False
        return pal
                
            