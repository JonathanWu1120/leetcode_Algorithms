class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        arr = {}
        counted = []
        for i,k in enumerate(s):
            if k not in arr:
                arr[k] = t[i]
                if t[i] not in counted:
                    counted.append(t[i])
                else:
                    return False
            elif k in arr:
                if arr[k] != t[i]:
                    return False
        return True