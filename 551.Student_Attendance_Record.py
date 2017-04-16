class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        a = 0
        for c in s:
            if c == "A":
                if a == 1:
                    return False
                a += 1
                l = 0
            elif c == "L":
                if l == 2:
                    return False
                l += 1
            else:
                l = 0
        return True
                