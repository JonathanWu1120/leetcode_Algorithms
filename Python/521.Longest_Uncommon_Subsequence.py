class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        c,d = len(a),len(b)
        if c == d and a == b:
            return -1
        return max(c,d)