class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = str.split(" ")
        if len(pattern) != len(s):
            return False
        arr = {}
        counted = []
        for i,k in enumerate(pattern):
            if k not in arr:
                arr[k] = s[i]
                if s[i] not in counted:
                    counted.append(s[i])
                else:
                    return False
            elif k in arr:
                if arr[k] != s[i]:
                    return False
        return True