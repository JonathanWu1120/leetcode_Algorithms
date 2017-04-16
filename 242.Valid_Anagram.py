class Solution(object):
    def mkarr(self,arr):
        d = {}
        for i in arr:
            if i not in d:
                d[i] = 1
            elif i in d:
                d[i] +=1
        return d
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) < len(t) or len(s) > len(t):
            return False
        arr1 = self.mkarr(s)
        arr2 = self.mkarr(t)
        for k,v in arr1.items():
            if k not in arr2:
                return False
            if v != arr2[k]:
                return False
        return True
            