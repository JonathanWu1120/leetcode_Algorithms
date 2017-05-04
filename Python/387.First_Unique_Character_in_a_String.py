class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = {}
        val = ""
        for c,k in enumerate(s):
            if k not in arr:
                arr[k] = True,c
            elif s[c] in arr:
                arr[k] = False,c
        min = float("inf")
        for k,v in arr.items():
            if v[0] == True:
                if v[1] < min:
                    min = v[1]
        if min == float("inf"):
            return -1
        return min